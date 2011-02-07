#! /usr/bin/env python
"""AsciiDoc filter script which runs the ditaa program to
convert ASCII line drawings into a PNG image file.

Requires the ditaa Java package to be present in the filter directory.

Copyright (C) 2011 Henrik Maier. Free use of this software is
granted under the terms of the GNU General Public License (GPL).
"""

usage = "%prog [options] inputfile"
__version__ = '1.1'

import os, sys, tempfile
from optparse import *


#
# Configuration constants
#
DITAA_JAR  = "ditaa0_9.jar"
DITAA_DIR  = os.path.dirname(os.path.realpath(sys.argv[0]))
DITAA_PATH = os.path.join(DITAA_DIR, DITAA_JAR)


#
# Global data
#
verbose = False


#
# Helper functions and classes
#
class AppError(Exception):
    """Application specific exception."""
    pass


def print_verbose(line):
    if verbose:
        sys.stderr.write(line + os.linesep)


def systemcmd(cmd):
    if not verbose:
        cmd += " 2>%s" % os.devnull
    cmd += " >&2" # redirect verbose output to stderr
    print_verbose("Exec: %s" % cmd)
    if os.system(cmd):
        raise AppError, "failed command: %s" % cmd


#
# Application init and logic
#
class Application():
    """Application class"""

    def __init__(self):
        """Process commandline arguments"""
        global verbose
        parser = OptionParser(usage, version="%%prog %s" % __version__)
        parser.add_option("-v", "--verbose", action="store_true",
                          help="verbose output to stderr")
        parser.add_option("-o", "--outfile", help="file name of the output file")
        parser.add_option("-A", "--no-antialias", action="store_true",
                          help="turns anti-aliasing off")
        parser.add_option("-E", "--no-separation", action="store_true",
                          help="prevents the separation of common edges of shapes")
        parser.add_option("-r", "--round-corners", action="store_true",
                          help="causes all corners to be rendered as round corners")
        parser.add_option("-s", "--scale", type=float, help="image scaling")
        parser.add_option("-S", "--no-shadows", action="store_true",
                          help="turns off the drop-shadow effect")
        parser.add_option("-t", "--tabs",
                          help="tabs are normally interpreted as 8 spaces but"
                          " it is possible to change that using this option")
        self.options, args = parser.parse_args()
        verbose = self.options.verbose
        print_verbose("Runing filter script %s" % os.path.realpath(sys.argv[0]))
        if len(args) != 1:
            parser.error("Invalid number of arguments")
        self.infile = args[0]
        if self.options.outfile is None:
            if self.infile == '-':
                parser.error("OUTFILE option must be specified")
            self.options.outfile = "%s.png" % os.path.splitext(self.infile)[0]
            print_verbose("Output file is %s" % self.options.outfile)


    def run(self):
        """Core logic of the application"""
        outfile = os.path.abspath(self.options.outfile)
        outdir = os.path.dirname(outfile)
        if not os.path.isdir(outdir):
            raise AppError, 'directory does not exist: %s' % outdir
        temp = None
        try:
            if self.infile == '-':
                source = sys.stdin.read()
                temp = tempfile.NamedTemporaryFile(delete=False)
                infile = temp.name
                print_verbose("Temporary input file is %s" % infile)
                temp.write(source)
                temp.close()
            else:
                infile = self.infile
            options = "--overwrite" # Always set
            if self.options.verbose:
                options += " -v"
            if self.options.no_antialias:
                options += " --no-antialias"
            if self.options.no_separation:
                options += " --no-separation"
            if self.options.round_corners:
                options += " --round-corners"
            if self.options.no_shadows:
                options += " --no-shadows"
            if self.options.scale:
                options += " --scale %f" % self.options.scale
            if self.options.tabs:
                options += " --tabs %d" % self.options.tabs
            systemcmd('java -jar "%s" "%s" "%s" %s' % (
                      DITAA_PATH, infile, outfile, options))
        finally:
            if temp:
                os.remove(temp.name)
        # To suppress asciidoc 'no output from filter' warnings.
        if self.infile == '-':
            sys.stdout.write(' ')


#
# Main program
#
if __name__ == "__main__":
    """Main program, called when run as a script."""
    try:
        app = Application()
        app.run()
    except KeyboardInterrupt:
        sys.exit("Ouch!")
    except Exception, e:
        sys.exit("%s: %s\n" % (os.path.basename(sys.argv[0]), e))

