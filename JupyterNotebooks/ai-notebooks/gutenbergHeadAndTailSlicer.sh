# Description: Removes the preamble and postscript from a specified Project 
# Gutenberg file creating a clean version in the same directory.
# Author: <Your Name>
# Last modified: <Date YOU created/modified this file>

# Take a file name as input
file=$1
	
# Find the start and end lines of the file with line numbers grep with -n flag
startNum=$(grep -n "START OF THIS PROJECT GUTENBERG" $file | cut -d: -f1)
endNum=$(grep -n "END OF THIS PROJECT GUTENBERG" $file | cut -d: -f1)

# Use the start and end lines to determine where to make the second cut
(( headCutNum = $endNum - $startNum ))
	
# Remove the .txt from the filename using a trick from 
# http://www.thegeekstuff.com/2010/07/bash-string-manipulation/
outFile=${file%.*}-clean.txt
	
	# Make the cuts and redirect to the output file
	head -$endNum $file | tail -$headCutNum > $outFile
