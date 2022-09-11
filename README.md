# ASM file parser

Converts ASM Text segment log into HDL program memory format.

Parser takes the QtSpim Text Segment log file and formats it line by line.
To get correct results, remove the head from the log, starting it from the actual real program that needs to be in memory (e.g. remove system instructions and assembly hardcoded inputs).

Parser also automatically substitutes the /jr $ra/ instruction with the correct /beq/, adds the dummy inst and the endless loop at the beginning.

Parser removes the Kernel segment from the log, no need to delete it manually.

To create a log file in QtSpim, go to "File" -> "Save log file". There, tick "Text segments" and choose the path to save the log.

For the parser to work:
* the log file should be in the same directory,
* the log file has to be named "asm"
This is all for the sake of speed. :)
