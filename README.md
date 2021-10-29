# Typo-v0.1
Typo version 0.1
Typo is an experimental programming language. Will receive new updates from time to time ;D


Brief overview of Typo v0.1 Syntax

BEGIN Keyword
Marks the start of the program.
If not included, raises a SyntaxError.

END Keyword
Marks the end of the program
If included before BEGIN keyword, raises SyntaxError.

PADD, PSUBTRACT, PMULTIPLY, PDIVIDE Keywords

Keywords that allow users to do basic mathematical operations and print the result.
If arguments are not integers, raises a TypeError.
If no or extra indentation at the start, it raises an IndentationError.
