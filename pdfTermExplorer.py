#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox as messagebox
import ttk

from os import listdir
from os.path import isfile, join

from pdfReader import searchPDFMiner
from SearchWord import SearchWord

from threading import Thread
import time

from collections import defaultdict
from multiprocessing.pool import ThreadPool

def startProcess(*args):
    error.set('')
    string = wordList.get()
    if string > 0:
        sw = SearchWord('')
        path = './pdfFolder/' # folder with the pdf to process
        saveFolder = './results/'
        files = [f for f in listdir(path) if isfile(join(path, f))]
        # Words passed as an argument comma separated, example 'Environmental justice, Justice, Knowledge'
        wordsToSearch = string
        # print wordsToSearch
        wordsToSearch = sw.splitWords(wordsToSearch)
        # print wordsToSearch
        # print wordsToSearch[0]

        termIndex = defaultdict(dict)
        totalFiles = len(files)
        filename = userfile.get()
        pool = ThreadPool(processes=totalFiles)
        if not len(filename) >= 0:
            filename = 'output'
        filename = saveFolder + filename + '.txt'

        writer = open(filename, 'w')

        for x in xrange(totalFiles):
            async_result = pool.apply_async(searchPDFMiner, (wordsToSearch, path, files[x]))

            progress.set(str(x + 1) + ' of ' + str(totalFiles))
            end.set('Processing file ' + files[x])
            root.update()

            wordsToSearch = async_result.get()
            writer.write('--Results for '+ files[x] + '--' + '\n')
            for y in xrange(len(wordsToSearch)):
                if wordsToSearch[y].occurrences > 0:
                    writer.write(str(wordsToSearch[y]) + '\n')
            writer.write('--------------------------\n')
            for z in xrange(len(wordsToSearch)): # Second output
                word = wordsToSearch[z].getWord()
                value = wordsToSearch[z].getOccurrences()
                doc = files[x]
                termIndex[word][doc] = value
                #Next document
                wordsToSearch[z].reset()        

        for term, documento in termIndex.items():
            total = 0
            # print '#########  '+ term +'  ##################'
            writer.write('#########  '+ term +'  ##################\n')
            for doc, value in documento.items():
                total += value
                if value > 0:
                    writer.write(str(value) + ' occurrence/s for the document ' + doc + '\n')
            writer.write('@@ The total number of occurrences of the term ' + term + ' is ' + str(total) + ' @@' + '\n')
        end.set('Process ended, the output is in ' + filename)
        
        writer.close()
    else:
        error.set('Please, set a term to look for')
    root.update()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
    
######################## Main ############################################3
root = Tk()
root.title("PDF Term searcher")
root.protocol("WM_DELETE_WINDOW", on_closing)

mainframe = ttk.Frame(root, padding="8 8 26 26")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

wordList = StringVar()
userfile = StringVar()
error = StringVar()
end = StringVar()
progress = StringVar()

ttk.Label(mainframe, text="Word List comma separated").grid(column=2, row=1)
# wordList_entry = Text(root)

wordList_entry = ttk.Entry(mainframe, width=60, textvariable=wordList)
wordList_entry.grid(column=2, row=2)

ttk.Label(mainframe, text="Filename to save the results").grid(column=2, row=3)

filename_entry = ttk.Entry(mainframe, width=30, textvariable=userfile)
filename_entry.grid(column=2, row=4)

ttk.Label(mainframe, textvariable=error).grid(column=2, row=5)
ttk.Button(mainframe, text="Search", command=startProcess).grid(column=2, row=5, sticky=(E))
ttk.Label(mainframe, textvariable=progress).grid(column=2, row=6)
ttk.Label(mainframe, textvariable=end).grid(column=2, row=7)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

wordList_entry.focus()
root.bind('<Return>', startProcess)

root.mainloop()

