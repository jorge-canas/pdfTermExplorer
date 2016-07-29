# pdfTermExplorer
Small app to look for terms in pdf files

# Graphic version: pdfTermExplorer.py

It has two input fields, one for the terms you want to look for (comma separated, it support compound words/phrases) and the other one for output file name (default filename is output.txt). This graphic version will look for any pdf in a folder called 'pdfFolder' and the results will be saved in a folder called 'results'

You can launched via launch.sh (with execution privileges) or via command using 'python pdfTermExplorer.py'

You will have two different outputs:
 - The first output will tell you, for each document, wich are the words/phrases found, how many times and in which pages
 - The second one will tell you, for each word/phrase, how many times does the word/phrase appears and in which document

Requirements Python 2.6, PDFMiner (the one used in this project is 20140328), Tkinter 81008

This project use PDFMiner to parse the pdf to text.

PDFMiner
Copyright (c) 2004-2014  Yusuke Shinyama <yusuke at cs dot nyu dot edu>
