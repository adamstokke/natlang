import urllib
from bs4 import BeautifulSoup
import nltk

def geturltext(url):
    response = urllib.urlopen(url)
    raw = response.read().decode('utf-8')

    doc = BeautifulSoup(raw)
    print 'document title: ', doc.title.string
    #print 'document head: ', doc.head
    #print 'document text: ', doc.get_text()

    tokens = nltk.word_tokenize(doc.get_text())
    print "# of tokens: ", len(tokens)
    #print tokens[:25]

    text = nltk.Text(tokens)
    print 'collocations: ', text.collocations()

    





