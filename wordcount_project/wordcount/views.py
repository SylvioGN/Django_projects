from django.http import HttpResponse 
from django.shortcuts import render
import operator

#def homepage(request):
#    return HttpResponse('Helloooooo!')


def homepage(request):
   return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    
    wordlist = fulltext.split()

    dicword = {}

    for x in wordlist:
        if x not in list(dicword.keys()): 
            dicword[x] = 1 
        else:
            dicword[x] +=  1

    sortedwords = sorted(dicword.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':sortedwords})

def about(request):
   return render(request, 'about.html')



