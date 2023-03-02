header = \
    "\\documentclass{article}\n\n" + \
    "\\usepackage[a4paper,top=2cm,bottom=2cm,left=3cm,right=3cm,marginparwidth=1.75cm]{geometry}\n" + \
    "\\usepackage[utf8]{inputenc}\n" + \
    "\\usepackage{amsmath}\n" + \
    "\\usepackage{amssymb}\n" + \
    "\\usepackage{float}\n" + \
    "\n\\renewcommand{\\thesection}{Question \\arabic{section}}\n" + \
    "\\renewcommand{\\thesubsection}{(\\alph{subsection})}\n" + \
    "\\renewcommand{\\thesubsubsection}{(\\roman{subsubsection})}\n" + \
    "\n\\setlength{\parindent}{0pt}\n"

alph = list('abcdefghijklmnopqrstuvwxyz')
roman = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']

# ----------- CHANGE THIS TO YOUR NAME -----------------
default_author = "Daniel Hewitt-Perraud"

# intro stuff
print("\nassignment latex generator\nsupports up to three levels of questions (i.e. Q2bi)\njust copy and rename template.tex or copy the contents to overleaf to use it\n\n")

# open/create and wipe file for writing then start the preamble
file = open("template.tex", "w")
file.write(header)

# get assignment name
assName = input("please enter the name of the assignment:\n")
file.write("\n\\title{" + assName + "}\n")

# get author
author = input("please your name: (leave blank for", default_author + " )\n")
if author == "":
    author = default_author
file.write("\\author{" + author + "}\n")

# get date
assDate = input("please enter the date the assignment is due: (probably just month and year)\n")
file.write("\\date{" + assDate + "}\n")

# start the main part
file.write("\n\\begin{document}\n\n\\maketitle\n")

# create question headings
validInput = False
while not validInput:
    try:
        numberOfQuestions = int(input("please enter the number of questions:\n"))
    except ValueError:
        print("invalid number of questions")
    else:
        validInput = True

for i in range(numberOfQuestions):
    print("QUESTION", i + 1, ":")
    file.write("\n\\section{} %Q"+ str(i + 1) + "\n")
    hasPart = input("    does Q" + str(i + 1) + " have any parts? (y/n) ")
    if hasPart == "y":
        validInput = False
        while not validInput:
            try:
                numberOfParts = int(input("    please enter the number of parts for Q" + str(i + 1) + ": "))
            except ValueError:
                print("    invalid number of parts")
            else:
                validInput = True
        for j in range(numberOfParts):
            file.write("\n\\subsection{} %Q"+ str(i + 1) + alph[j] + "\n\n")
            hasSubpart = input("    does Q" + str(i + 1) + alph[j] + " have any subparts? (y/n) ")
            if hasSubpart == "y":
                validInput = False
                while not validInput:
                    try:
                        numberOfSubparts = int(input("    please enter the number of subparts for Q" + str(i + 1) + alph[j] + ": "))
                    except ValueError:
                        print("    invalid number of subparts")
                    else:
                        validInput = True
                for k in range(numberOfSubparts):
                    file.write("\n\\subsubsection{} %Q"+ str(i + 1) + alph[j] + roman[k] + "\n\n")
    else:
        file.write("\n")

#end doc
file.write("\n\\end{document}")
file.close()

print("latex template successfully generated")
