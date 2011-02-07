ditaa filter for AsciiDoc
=========================
Author: Henrik Maier

Version: 1.1


Introduction
------------

ditaa (link:http://ditaa.sourceforge.net[]) is a small command-line utility
written in Java, that can convert diagrams drawn using ascii art (drawings
that contain characters that resemble lines like | / - ), into proper bitmap
graphics.

Using the AsciiDoc ditaa filter, ASCII line art can be embedded into AsciiDoc
documents and processed as PNG bitmap graphics.
Ditaa as of version 0.9 is limited to the PNG format as output.

Usage
-----

- The ditaa filter is invoked by setting the listing block or
  paragraph style (the first positional block attribute) to '"ditaa"'.
- The second positional attribute (named 'target') is optional, it sets
  the name of the generated image file. If this is not supplied a
  file name is automatically generated.
- Additional well known ditaa options can be specified as named attributes. Refer to table below.

.Supported ditaa options
[cols="20e,35m,45",options="header,unbreakable"]
|==============================================================================
| Option        | Example                           | Function
| scaling       | ["ditaa",scaling="2.0"]           | ditaa image scaling
    footnote:[`scaling` is different to the DocBook backend's image `scale` attribute!]
| tabs          | ["ditaa",tabs="4"]  | tabs are normally interpreted as 8 spaces but
                                        it is possible to change that using this option
| round-corners | ["ditaa",options="round-corners"] | causes all corners to be rendered as round corners
| no-separation | ["ditaa",options="no-separation"] | prevents the separation of common edges of shapes
| no-shadows    | ["ditaa",options="no-shadows"]    | turns off the drop-shadow effect
| no-antialias  | ["ditaa",options="no-antialias"]  | turns anti-aliasing off
|==============================================================================


This AsciiDoc block:

.....................................................................
["ditaa"]
---------------------------------------------------------------------
    +--------+   +-------+    +-------+
    |        | --+ ditaa +--> |       |
    |  Text  |   +-------+    |diagram|
    |Document|   |!magic!|    |       |
    |     {d}|   |       |    |       |
    +---+----+   +-------+    +-------+
        :                         ^
        |       Lots of work      |
        +-------------------------+
---------------------------------------------------------------------
.....................................................................

renders:

["ditaa"]
---------------------------------------------------------------------
    +--------+   +-------+    +-------+
    |        | --+ ditaa +--> |       |
    |  Text  |   +-------+    |diagram|
    |Document|   |!magic!|    |       |
    |     {d}|   |       |    |       |
    +---+----+   +-------+    +-------+
        :                         ^
        |       Lots of work      |
        +-------------------------+

---------------------------------------------------------------------


Installation
------------

In addition to AsciiDoc you will need to have installed:

- Java
- The ditaa 0.9 jar package (link:http://ditaa.sourceforge.net[])
  must be present in the filter directory. It is included in this
  filter distribution for convenience.
  The GPL licensed ditaa source code can be obtained from
  http://sourceforge.net/projects/ditaa/[].


The filter was developed and tested on Windows using ditaa 0.9
and AsciiDoc 8.6.3.


Examples
--------

The following examples are taken from the ditaa documentation.

.Blocks
["ditaa"]
-------------------------------------------------------------------------------
+---------+
| cBLU    |
|         |
|    +----+
|    |cPNK|
|    |    |
+----+----+
-------------------------------------------------------------------------------


.Round corners
["ditaa"]
-------------------------------------------------------------------------------
/--+
|  |
+--/
-------------------------------------------------------------------------------

.Color
["ditaa"]
-------------------------------------------------------------------------------
/----\ /----\
|c33F| |cC02|
|    | |    |
\----/ \----/

/----\ /----\
|c1FF| |c1AB|
|    | |    |
\----/ \----/
-------------------------------------------------------------------------------


.Color codes
["ditaa"]
-------------------------------------------------------------------------------
Color codes
/-------------+-------------\
|cRED RED     |cBLU BLU     |
+-------------+-------------+
|cGRE GRE     |cPNK PNK     |
+-------------+-------------+
|cBLK BLK     |cYEL YEL     |
\-------------+-------------/
-------------------------------------------------------------------------------


.Dashed lines
["ditaa"]
-------------------------------------------------------------------------------
----+  /----\  +----+
    :  |    |  :    |
    |  |    |  |{s} |
    v  \-=--+  +----+
-------------------------------------------------------------------------------


.Point markers
["ditaa"]
-------------------------------------------------------------------------------
*----*
|    |      /--*
*    *      |
|    |  -*--+
*----*
-------------------------------------------------------------------------------


.Text handling
["ditaa"]
-------------------------------------------------------------------------------
/-----------------\
| Things to do    |
| cGRE            |
| o Cut the grass |
| o Buy jam       |
| o Fix car       |
| o Make website  |
\-----------------/
-------------------------------------------------------------------------------


.Flowchart
["ditaa"]
-------------------------------------------------------------------------------
            +-------+
+-------+   |       |    +---------+
|cFDA   |   |{c}    |    |eat cFF8 +
|wake up+-->+hungry?+--->|breakfast|
| {o}   |   | cDBF  |Y   +----+----+
+-------+   |       |         |
            +---+---+         v
                |N       +-----------+
                +------->| save c9FB |
                         | planet{mo}|
                         +-----------+
-------------------------------------------------------------------------------


.Shapes
["ditaa"]
-------------------------------------------------------------------------------
 +----+---+----+----+---+---+---+
 |    |{o}|    |    |{c}|{s}|   |
 |{tr}|   |{mo}|{io}|   |   |{d}|
 +----+---+----+----+---+---+---+
-------------------------------------------------------------------------------

