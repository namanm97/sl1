# 3B
# Write a python program to read contents of a file (filename as argument) and
# store number of occurrences of each word in a dictionary. Display the top 10
# words with most number of occurrences in descending order. Store the length of
# each of these words in a list and display the list. Write a one-line reduce
# function to get the average length and one-line list comprehension to display
# squares of all odd numbers and display both.


import sys
import os
import functools

if(len(sys.argv) != 2):
	print ("Invalid Arguments")
	sys.exit()

if(not(os.path.exists(sys.argv[0]))):
	print ("Invalid File Path")
	sys.exit()

if(sys.argv[1].split('.')[-1] != "txt"):
	print ("Invalid File Format. Only TXT files allowed")
	sys.exit()

escape = open(sys.argv[1])

worddic = { }
# 1 (ii) Store number of occurrences of each word in a dictionary.

 for line in escape: #Outer for loop - taking each line in the file
 #print (line )
 myline = line.split()  #myline is a list containg the words split - space is delimiter
 #print (myline)

 for word in myline: #Inner for-loop processing each line
 w = worddic.get(word,0) #'0' is the default value put in the value part, in case the word is encountered for first time
  #print ("key word %s exists in doctionary with %d value" %(word, w))

  worddic[word] = w + 1 #Incrementing the word count, if the word exists
  #print (worddic[word] )

print ("\n Result of storing number of occurances of word in dictionary \n", worddic ,"\n ")


#2 top 10 words with most number of occurences in descening order

sortedlist = [ ]

sortedlist = sorted(worddic.items(), key = lambda Y : Y[1], reverse = True)
print ("\n Sorting in Dscending order of Value Occurance - \n" )
for n in range(0,10):
 	print (sortedlist[n], "\n")

#3 Length of each word in a list and display the list
lenlist = []
print ("\n Length of each word in a list \n")
for i in range(len(sortedlist)):

		wordTuple = sortedlist[i]
		print ("\n ", wordTuple[0], ", Frequency: " , wordTuple[1] , ", Length " , len(wordTuple[0]))
		lenlist.append(len(wordTuple[0]))

#4  one-line reduce function to get the average length of the words

mysum = functools.reduce(lambda x, y: x + y, lenlist)
print ("\n Average length of all words: " , mysum/len(lenlist))

# 1 (Vii) one-line list comprehension to display squares of all odd numbers

squares = [x**2 for x in lenlist if x%2 != 0]
print ("\n Squres of odd word lengths: ")
print (squares)
