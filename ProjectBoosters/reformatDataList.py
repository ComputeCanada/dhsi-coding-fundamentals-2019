# this is a program to reformat free text data into a readable csv
# it requires the "free text" to actually have consistent formatting that is known to the programmer
# this program is tailored to deal with a .txt file in the following format

#Record 1 of 50
#CALL #       MF-14291.
#TITLE        The overseas Hindustan times [microform]
#IMPRINT      New Delhi : Hindustan Times Ltd., -1987.

#Record 2 of 50
#CALL #       MF.
#TITLE        The searchlight [microform]
#IMPRINT      Patna : The Behar Journals, Ltd., [1918-1986]

# open text file in read-only mode, create a list of all the lines in the file
readFile = open("text.txt")
contents = readFile.readlines()

# open a csv file to write results to
writeFile = open("reformattedtext.csv","w")
writeFile.write("RECORD,CALL #,TITLE,IMPRINT\n")

# loop through the list of lines
for line in contents:
    # check to see if it's one of a predetermined set of line options, process text varying ways
    if line[0] == "R":
        writeFile.write(line[7] + ",") #example if I know I want one character from a specific place
    elif line[0] == "C":
        words = line.split(" ") #split on spaces into a list of words from the line
        callNumber = words[-1].strip("\n") #takes last word from line, removes newline character from end of word
        writeFile.write(callNumber + ",") #example if I want the final word in a series of words
    elif line[0] == "T":
        words = line.split("        ") #split on a tab or some other large number of spaces
        title = words[1].strip("\n") #takes second/last word from line, removes newline character from end of word
        writeFile.write('"' + title + '"' + ',') #added "" around title in case of commas
    elif line[0] == "I":
        words = line.split("IMPRINT      ") #remove first part of the string
        words = words[1].strip("\n") # remove newline character and save over same variable name
        writeFile.write('"' + words + '"' + "\n") #added "" around imprint in case of commas

# close the files so we don't accidentally corrupt them or crash something
readFile.close()
writeFile.close()