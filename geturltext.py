#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import nltk

def geturltext(url):
    """Given a valid url, print information about the textual content
       contained within the data found at that url. Not guaranteed,
       at present, to resturn 'optimal' results."""
    response = urllib.urlopen(url)
    raw = response.read().decode('utf-8')

    doc = BeautifulSoup(raw)
    print 'document title: ', doc.title.string, '\n'
    #print 'document head: ', doc.head
    #print 'document text: ', doc.get_text()

    tokens = nltk.word_tokenize(doc.get_text())
    print "# of tokens: ", len(tokens)

    text = nltk.Text(tokens)
    print 'collocations: ', text.collocations()

    # here, prune the words by getting rid of code bits that show
    # up as words (see nltk book 3.4, etc.)
    somewords = [w for w in text if "=" not in w]
    somewords = [w for w in somewords if "." not in w]
    somewords = [w for w in somewords if "_" not in w]
    somewords = [w for w in somewords if "+" not in w]
    somewords = [w for w in somewords if "/" not in w]
    
    words = [w.lower() for w in somewords]
    vocab = sorted(set(words))

    print "# of unique words: ", len(vocab), '\n'

    #print vocab

    





