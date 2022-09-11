# ASM file parser

Converts ASM Text segment log into HDL program memory format.

Parser takes the QtSpim Text Segment log file and formats it line by line.

To create a log file in QtSpim, go to "File" -> "Save log file". There, tick "Text segments" and choose the path to save the log.

To get correct results, remove the head from the log, starting it from the actual real program that needs to be in memory (e.g. remove system instructions and assembly hardcoded inputs). The log should start with the first real instruction of your code.

Changes that the parser makes to the instructions:
* Automatically substitutes the /jr $ra/ instruction with the correct /beq/
* Adds the dummy instruction and the endless loop at the beginning
* Removes the Kernel segment from the log (no need to delete it manually)

For the parser to work:
* the log file should be in the same directory,
* the log file has to be named "asm"
This is all for the sake of speed. :)
