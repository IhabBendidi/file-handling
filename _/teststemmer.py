import argparse
import porterstemmer as stemmer



def main():

	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i",type=str, required=True,
		help="path to inputfile for the first task")
	ap.add_argument("-s", type=str, default="stopword_list.txt",
		help="The path to the stopword list used for the task")
	args = vars(ap.parse_args())


	s=open(args["s"], "r")

	if s.mode == 'r':
		stopwords =s.readlines()
		for j in range(len(stopwords)):
			stopwords[j] = stopwords[j].split("\n")[0]
			stopwords[j] = stopwords[j].split("\t")[0]
	else:
		return "error reading stopwords file"

	p = stemmer.PorterStemmer()

	i=open(args["i"], "r")
	if i.mode == 'r':
		contents =i.readlines()
		for line in contents:

			document = line

			words = document.split(" ")
			for j in range(len(words)):
				words[j] = words[j].split(".")[0]
				words[j] = words[j].split(",")[0]
				words[j] = words[j].split("!")[0]
				words[j] = words[j].split(":")[0]
				words[j] = words[j].split("?")[0]
				words[j] = words[j].split(";")[0]
				words[j] = words[j].split("/")[0]
				words[j] = words[j].split("\n")[0]
				words[j] = words[j].lower()

			word_list = []
			for word in words :
				if word not in stopwords :
					if not word.isnumeric():
						word_list.append(word)

			for j in range(len(word_list)):
				word_list[j] = p.stem(word_list[j], 0,len(word_list[j])-1)
			print(word_list)
	else :
		return "error reading input file"







if __name__ == "__main__":
	main()
