#Sorting string

import string
from collections import OrderedDict

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"," "]

sentence = raw_input("Enter your sentence: ")


#take out spaces and punctuations
for i in punctuation:
    sentence = sentence.replace(i,"")

#get unique letters
od = OrderedDict.fromkeys(sentence).keys()


countarray= []

#multiply count by unique letter
for i in od:
    count=sentence.count(i)
    numlet = count*i
    countarray.append(numlet)

countarray = sorted(countarray)

print "".join(countarray)
