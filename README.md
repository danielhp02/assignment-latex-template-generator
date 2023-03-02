# assignment-latex-template-generator
Prompts user for inputs to create a latex template suitable for a maths or science assignment. Currently supports up to 3 levels of questions, e.g. Q2bi. At the moment, the first level is numeric, second is a letter (so up to 26 parts), and third is a roman numeral (up to x).

## Setup
Just change the default author on line 17 to the one that will be most frequently used. This is optional, as the script prompts the user for an author each time it is run anyway.

## Usage
Just run it and follow the prompts. Once finished, the output is saved to template.tex in the directory the script was called from.
