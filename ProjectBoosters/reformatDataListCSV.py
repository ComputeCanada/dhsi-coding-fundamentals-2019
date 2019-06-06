# this is a program to reformat csv data into a readable csv

import csv

# open csv file of places and read stuff

originFile = open("text.csv")
textReader = csv.reader(originFile)

# open a csv file to write results to
writeFile = open("reformattedtext.csv","w")
writeFile.write("Whatever,Columns,You,Want Here\n")

# loop through rows; check conditions and do stuff based on what you find in the rows
for row in textReader:
    try:
        if row[0]== "GET ME OUTTA THIS ROW!":
            words = row[0].split(" ") #split on spaces into a list of words from the line
            finalWord = words[-1] # take the final word
            finalWord = finalWord.strip("!") # removes the !
            writeFile.write(finalWord+"\n") # return the final word and start a new line
        elif row[0] == "":
            writeFile.write("empty first cell!\n")
        elif float(row[1]) <= 0:
            if float(row[0]) != 0:
                writeFile.write(",yo western hemisphere!\n")
            else:
                writeFile.write("Greenwich Mean Line!")
        else:
            writeFile.write("bummer, I don't know what to do\n")
    except:
        writeFile.write("FYI I'm skipping this row\n")

# close the files so we don't accidentally corrupt them or crash something
originFile.close()
writeFile.close()