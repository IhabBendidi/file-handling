import argparse
import porterstemmer as stemmer # importing the stemmer given in the link in the instructions  https://tartarus.org/martin/PorterStemmer/index.html



def main():

	# construct the argument parser and parse the arguments (input, output path and stopwords)
	ap = argparse.ArgumentParser()
	ap.add_argument("-i",type=str, required=True,
		help="path to inputfile for the first task")
	ap.add_argument("-o",type=str, required=True,
		help="path to output file if it exists, if not, it will be created")
	ap.add_argument("-s", type=str, default="stopword_list.txt",
		help="The path to the stopword list used for the task")
	args = vars(ap.parse_args())




	#opening the stopwords file and preparing the stopwords inside
	s=open(args["s"], "r")
	if s.mode == 'r':
		stopwords =s.readlines()
		for j in range(len(stopwords)):
			stopwords[j] = stopwords[j].split("\n")[0]
			stopwords[j] = stopwords[j].split("\t")[0]
	else:
		return "error reading stopwords file"



	# Initializing the stemmer tool
	p = stemmer.PorterStemmer()




	# Opening the input file
	i=open(args["i"], "r")
	if i.mode == 'r':
		# Reading the lines in the input file
		contents =i.readlines()

		#Initializing the output variables
		titles = []
		output_doc = []

		#Parsing the lines and preprocessing the content
		for line in contents:
			title,document = line.split("\t")
			titles.append(title)
			words = document.split(" ")
			for j in range(len(words)):
				words[j] = words[j].split(".")[0]
				words[j] = words[j].split(",")[0]
				words[j] = words[j].split("!")[0]
				words[j] = words[j].split(":")[0]
				words[j] = words[j].split("?")[0]
				words[j] = words[j].split(";")[0]
				words[j] = words[j].split("/")[0]
				temp = words[j].split('"')
				if len(temp)>1 :
					words[j] = temp[1]
				else :
					words[j] = temp[0]
				words[j] = words[j].split("\n")[0]
				words[j] = words[j].lower()

			word_list = []

			# Eliminating stopwords and numerical values
			for word in words :
				if word not in stopwords :
					if not word.isnumeric():
						word_list.append(word)

			# Stemming the content
			for j in range(len(word_list)):
				word_list[j] = p.stem(word_list[j], 0,len(word_list[j])-1)

			output_doc.append(word_list)
	else :
		return "error reading input file"


	# Opening the output file ( or creating it if it doesnt exist)
	o=open(args["o"], "w+")

	# organizing output lines
	for (title,doc) in zip(titles,output_doc):
		output_line = title + "\t"
		for j in range(len(doc)):
			output_line += doc[j]
			if j<len(doc)-1 :
				output_line += " "

		# Writing the outputs in the output file
		o.write(output_line + "\n")

	# Closing the file readers
	o.close()
	i.close()
	s.close()







if __name__ == "__main__":
	main()
