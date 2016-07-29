#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

# from SearchWord import SearchWord

from utils import *

def searchPDFMiner(wordsList, path, pdf):
    # print 'Procesando '+ pdf
    filepath = path + pdf
    try:
        pageNumber = 0
        page = convert(filepath, pages=[pageNumber])
        while len(page) > 0:
            pageNumber += 1
            
            # print page
            for x in xrange(len(wordsList)):
                p = wordsList[x].getWord()

                palabras = cleanWords(page)

                if ' ' in p:
                    parts = p.split(' ')
                    for y in xrange(len(palabras)):
                        if parts[0] == palabras[y]:
                            equals = True
                            for z in xrange(len(parts)):
                                if parts[z] != palabras[y+z]:
                                    equals = False
                                    break
                            if equals:
                                wordsList[x].incOccurrences()
                                wordsList[x].addPage(pageNumber)
                else:
                    for palabra in palabras:
                        #if p in palabra:
                        if p == palabra:
                            # print wordsList[x]
                            wordsList[x].incOccurrences()
                            wordsList[x].addPage(pageNumber)
            # next page
            page = convert(filepath, pages=[pageNumber])

        return wordsList
        """
        print '--Resultados para '+ pdf + '--'
        for x in xrange(len(wordsList)):
            if wordsList[x].occurrences > 0:
                print wordsList[x]
        print '--------------------------'
        """
    except:
        print 'Hay un error con el fichero ' + pdf + '\n'
        return wordsList