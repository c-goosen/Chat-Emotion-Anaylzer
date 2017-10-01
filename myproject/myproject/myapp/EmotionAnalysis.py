
import codecs
import matplotlib.pyplot as plt
import numpy as np
import indicoio
indicoio.config.api_key = 'eb27e86cef4588d15c7e9933b1e1fefd'


def text_extract(filename):
	global name1
	global name2

	x = 1
	i = 1
	removefirst = 0

	person1 = []
	person2 = [] 
	combined = []#Declare an empty list named "lines"
	#with open (filename, 'r', "utf-8-sig") as in_file:
	arq = (codecs.open(filename, "r","utf-8-sig"))
	content = arq.read()
	arq.close()
	in_file = content.split("\n")


		# person1 = in_file[1] 
		# firstdash = person1.find("-")
		# replacedtext = person1.replace(":",".",1)
		# name1 = person1[firstdash:replacedtext.find(":")+1]
	 #Open file lorem.txt for reading of text data
	for line in in_file:
		if (removefirst == 1):
			firstdash = line.find("-")
			linex = line.replace(":",".",1)
			if (x==1): 
				name1 = line[firstdash+1:linex.find(":")]
				x = 0
			name3 = line[firstdash+1:linex.find(":")]
			if ((name1 != name3) and (i==1) ):
				name2 =name3
				i = 0
			linenew = line[linex.find(":")+1:-1]
			if (name1 == line[firstdash+1:linex.find(":")]):
				if (linenew != ""):
					person1.append(linenew)
			else:
				if (linenew != ""):
					person2.append(linenew) 
		else:
			removefirst = 1
	combined.append(person1)
	combined.append(person2)
	return (combined)


def collector(array):
	Angertot = 0
	Joytot = 0 
	Surprisetot = 0
	Sadnesstot = 0
	feartot = 0

	resultarray =[]

	arrsize = len(array)

	for z in range(0,arrsize):

		Angertot += array[z]['anger']
		Joytot += array[z]['joy']
		Surprisetot += array[z]['surprise']
		Sadnesstot += array[z]['sadness']
		feartot += array[z]['fear']

	resultarray.append(round((Angertot/arrsize)*100,0))
	resultarray.append(round((Joytot/arrsize)*100,0))
	resultarray.append(round((Surprisetot/arrsize)*100,0))
	resultarray.append(round((Sadnesstot/arrsize)*100,0))
	resultarray.append(round((feartot/arrsize)*100,0))

	return(resultarray)


def graph(array1,array2):
	name11 =name1
	name22 = name2
	n_groups = len(array1)
	fig, ax = plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.35
	opacity = 0.8
	rects1 = plt.bar(index, array1, bar_width,alpha=opacity,color='b',label=name11)
	rects2 = plt.bar(index + bar_width, array2, bar_width,alpha=opacity,color='g',label=name22)
	plt.xlabel('Person')
	plt.ylabel('Scores')
	plt.title('Scores by person')
	plt.xticks(index + bar_width, ('Anger', 'Joy', 'Surprise', 'Sad', 'Fear'))
	plt.legend()
	plt.tight_layout()
	plt.savefig("food.png")
	# plt.show()

def printgraph(filename):
	x = collector(indicoio.emotion((text_extract(filename))[0]))
	y = collector(indicoio.emotion((text_extract(filename))[1]))
	graph(x,y)


# x = collector(indicoio.emotion((text_extract("WhatsApp.txt"))[0]))
# y = collector(indicoio.emotion((text_extract("WhatsApp.txt"))[1]))

# graph(x,y)