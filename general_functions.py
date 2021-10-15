import numpy as np
import pandas as pd
import csv
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


name_of_csv='groupchat.csv'


#generates a new csv document called "groupchat_modified.csv" that has all messages as strings and 
#all hyperlinks removed
def refineChat(chat):
	#this fixes a glitch where not all messages are of type: string
	chat['message'] = chat['message'].map(lambda x: str(x))
	#removes all https links (optional)
	chat['message'] = chat['message'].map(lambda x:  x.split("https",1)[0])

	#removes all empty strings
	chat = chat[chat.message != '']

	chat.to_csv('groupchat_modified.csv',encoding="utf8")

#generates a word cloud of the words typed into the chat
def generateWordCloud(chat):
	stopwords = set(STOPWORDS)
	stopwords.update(["https", "lh3", "googleusercontent", "one", "lol","jpg","thats","conversation","s0","ok","changed","removed","user","png"])
	text = " ".join(str(message).lower() for message in chat.message)

	# Create and generate a word cloud image:
	wordcloud = WordCloud(max_font_size=400, max_words=1000, 
		background_color="white", stopwords=stopwords,
		width=1600, height=800).generate(text)

	# Display the generated image:
	plt.figure(figsize=[160,80])
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	plt.show()

#creates a DataFrame with two columns, the user's name and the title they named the chat to
def getPreviousChatNames(chat):
	chat = chat[chat.message_type == "RENAME_CONVERSATION"]
	chat['message'] = chat['message'].map(lambda x: str(x))
	chat['message_type'] = chat['message'].map(lambda x: str(x))
	chat['message'] = chat['message'].map(lambda x:  x.rsplit("to",1)[1].replace("\'",""))
	return(chat.drop(['unixtime','timestamp','message_type','message_html','sender_id'],axis=1))

def word_count(str):
	count=0
	words = str.split()
	for word in words:
		count+=1
	return (count)

#returns a zipped list of (user,how many messages they have sent)
#does not use pandas, not efficient, should be changed in a later version to involve the pd library
def getUserChatFrequencies():
	users = []
	chatFreq=[]

	with open(name_of_csv, newline='',encoding="utf8") as csvfile:
		gcreader=csv.reader(csvfile, delimiter=';')
		for row in gcreader:
			if (row[3] not in users):
				users.append((row[3]))
				chatFreq.append(1)
			else:
				chatFreq[users.index(row[3])]+=1

	#create list of people, int(chats sent)
	userFreq=zip(users,chatFreq)
	userFreq_sorted=sorted(userFreq, key=lambda x: x[1], reverse=True)
	for i in userFreq_sorted:
		print(i[0]+" sent "+str(i[1])+" messages and is #" + str(userFreq_sorted.index(i)+1))
	return(userFreq_sorted)


#returns a zipped list of (users,total word count)
#does not use pandas, not efficient, should be changed in a later version to involve the pd library
def getUserWordCounts():
	users = []
	wordCount=[]

	with open(name_of_csv, newline='',encoding="utf8") as csvfile:
		gcreader=csv.reader(csvfile, delimiter=';')
		for row in gcreader:
			if("REGULAR" in row[4]):
				if (row[3] not in users):
						users.append((row[3]))
						wordCount.append(word_count(row[5]))
				else:
					wordCount[users.index(row[3])]+=word_count(row[5])
		print("the loop has run")
	#create list of people, int(words sent)
	userWords=zip(users,wordCount)
	userWords_sorted=sorted(userWords, key=lambda x: x[1], reverse=True)
	for d in userWords_sorted:
		print(d[0]+" sent "+ str(d[1])+" words and is #" + str(userWords_sorted.index(d)+1))
	return(userWords_sorted)

#Returns a zipped list of (users,words per message avg)
#does not use pandas, not efficient, should be changed in a later version to involve the pd library
def getUserWordsPerMessage():
	users = []
	chatFreq=[]
	wordCount=[]
	wpm=[]
	with open(name_of_csv, newline='',encoding="utf8") as csvfile:
		gcreader=csv.reader(csvfile, delimiter=';')
		for row in gcreader:
			if("REGULAR" in row[4]):
				if (row[3] not in users):
					users.append((row[3]))
					chatFreq.append(1)
					wordCount.append(word_count(row[5]))
				else:
					chatFreq[users.index(row[3])]+=1
					wordCount[users.index(row[3])]+=word_count(row[5])
	#create list of people, double(words per message)
	for name in users:
		g=users.index(name)
		wpm.append(wordCount[g]/chatFreq[g])

	userWPM=zip(users,wpm)
	userWPM_sorted=sorted(userWPM, key=lambda x: x[1], reverse=True)

	#prints it out just for fun
	for k in userWPM_sorted:
		print(k[0]+" sent "+ str(k[1])+" avg words per message and is #" + str(userWPM_sorted.index(k)+1))

	return(userWPM_sorted)

#THIS IS WHERE THE FUN BEGINS

#if you want this to actually effect the user functions, the user functions must be rewritten to 
#work with the modified format

#refineChat(gc)

#gives fun stats!
#userChatFrequencies()
#userWordCounts()
#userWordsPerMessage()

#word cloud!!! edit the STOPLIST if you want to remove specific words
#generateWordCloud(gc)

#this will show you the first and last 5 chat names, you can do pm anything with this ...
#including make a csv with the information
#print(getPreviousChatNames(gc).head())
#print(getPreviousChatNames(gc).tail())
