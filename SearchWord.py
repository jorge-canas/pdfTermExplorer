#!/usr/bin/python
# -*- coding: utf-8 -*-

class SearchWord:
    word = ''
    occurrences = 0

    def __repr__(self):
        return self.word

    def __str__(self):
        pagesList = ''
        for page in self.pages:
            pagesList += str(page) + ', '
        if self.occurrences > 0:
            return 'The word(s) \"' + self.word + '\" appear(s) a total of ' + str(self.occurrences) + ' time(s). It appear(s) in the page(s) ' + pagesList[:-2]
        else:
            return 'The word/phrase \"' + self.word + '\" does not appear in the pdf '
    
    def addPage(self, num):
        if num not in self.pages:
            self.pages.append(num)

    def incOccurrences(self):
        self.occurrences += 1

    def __init__(self, word):
        self.word = word
        self.pages = [] #Needed here or the pages will be shared for all the objects

    def getWord(self):
        return self.word

    def getOccurrences(self):
        return self.occurrences

    def splitWords(self, text):
        wordList = text.lower().split(',')
        words = []
        for word in wordList:
            searchWord = SearchWord(word.strip())
            words.append(searchWord)
        return words
    
    def reset(self):
        self.occurrences = 0
        self.pages = []