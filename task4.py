import argparse
import math





def main():

    # construct the argument parser and parse the arguments (input, output path )
    ap = argparse.ArgumentParser()
    ap.add_argument("-i",type=str, required=True,
        help="path to inputfile for the fourth task")
    ap.add_argument("-a",type=str, required=True,
        help="first document")
    ap.add_argument("-b",type=str, required=True,
        help="second document")
    args = vars(ap.parse_args())

    # Opening the input file
    i=open(args["i"], "r")

    # retrieving docs
    doc1 = args["a"]
    doc2 = args["b"]

    if i.mode == 'r':
        # Reading the lines in the input file
        contents =i.readlines()



        # Main task : Extracting the two docs columns

        titles = contents[0].split("\t")[1:][:-1]

        # Setting booleans for checking the existence of the doc names that are prompted
        exists1 = False
        exists2 = False

        for j in range(len(titles)):

            if titles[j]==doc1:
                index1 = j
                exists1 = True
            elif titles[j]==doc2:
                index2 = j
                exists2 = True


        # Stopping the script if the documents do not exist in the input file
        if not exists1:
            print( "The first document does not exists in the input file")
            return "The first document does not exists in the input file"
        if not exists2:
            print( "The second document does not exists in the input file")
            return "The second document does not exists in the input file"


        # Setting up vectors for the data of the two documents
        document1 = []
        document2 = []
        # retriving data of the two documents
        for line in contents[1:]:
            weight1 = line.split("\t")[1:][index1].split("\n")[0]
            weight2 = line.split("\t")[1:][index2].split("\n")[0]
            document1.append(float(weight1))
            document2.append(float(weight2))


        # Computing the dot product of the documents
        dot_product = sum([i*j for (i, j) in zip(document1, document2)])

        # Computing the true value of each document

        true_value1 = math.sqrt(sum([math.pow(i,2) for i in document1]))
        true_value2 = math.sqrt(sum([math.pow(i,2) for i in document2]))


        # Computing cosine value
        cosine = dot_product / (true_value1*true_value2)

        print(cosine)

















    else :
        return "error reading input file"









    # Closing the file readers
    i.close()
if __name__ == "__main__":
	main()
