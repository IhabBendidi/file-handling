import argparse
import math



def main():

    # construct the argument parser and parse the arguments (input, output path )
    ap = argparse.ArgumentParser()
    ap.add_argument("-i",type=str, required=True,
        help="path to inputfile for the third task")
    ap.add_argument("-o",type=str, required=True,
        help="path to output file if it exists, if not, it will be created")
    args = vars(ap.parse_args())


    # Opening the input file
    i=open(args["i"], "r")
    # Opening the output file ( or creating it if it doesnt exist)
    o=open(args["o"], "w+")
    if i.mode == 'r':
        # Reading the lines in the input file
        contents =i.readlines()
        # Getting the titles of the documents and word count for each document
        header_titles = []

        # Variables for use later on
        dc = []
        wd = []
        dc.append([contents[0].split("\t")[0],len(contents[0].split("\t")[1:])])

        temp = contents[0].split("\t")[1:]
        for t in temp :
            t = t.split("\n")[0]
            header_titles.append(t)
            wd.append([t,1])

        for line in contents[1:] :
            dc.append([line.split("\t")[0],len(line.split("\t")[1:])])
            temp = line.split("\t")[1:]
            for t in temp :
                t = t.split("\n")[0]
                exists = False
                for header in header_titles :
                    if t == header:
                        exists = True
                        break
                if not exists :
                    header_titles.append(t)
                    wd.append([t,1])
                else :
                    for j in range(len(wd)):
                        if t == wd[j][0]:
                            wd[j][1] += 1



        #Writing the titles
        title_line = "\t"
        for j in range(0,len(header_titles)):
            title_line += header_titles[j]
            if j<len(title_line)-1 :
                title_line += "\t"

        o.write(title_line + "\n")



        #Preparing the TF-IDF weights variables


        # Number of times a word appears in a document
        word_cardinality = []
        for line in contents :
            vector = []
            for head in header_titles:
                exists = 0
                for word in line.split("\t")[1:]:
                    word = word.split("\n")[0]
                    if head == word :
                        exists = 1
                        break
                    else :
                        exists =0
                vector.append(exists)
            word_cardinality.append(vector)






        # Total number of documents
        total_num_docs = len(header_titles)

        # For each word, the number of docs it appears in
        doc_card = dc


        # the word count in each document
        word_count = wd

        # Computing final outputs
        output_weights = []



        for j in range(len(doc_card)):
            weight_line = []
            weight_line.append(doc_card[j][0])
            for k in range(len(word_count)):
                # IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
                IDF = round(math.log(total_num_docs/doc_card[j][1]),3)

                # TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)
                TF = round(word_cardinality[j][k]/word_count[k][1],3)

                # TF-IDF weight
                weight = round(IDF*TF,3)

                weight_line.append(weight)

            output_weights.append(weight_line)



        # Saving the weights in the output file
        for w in output_weights:
            output_line = w[0] + "\t"
            for j in range(1,len(w)):
                output_line += str(w[j])
                if j<len(w)-1:
                    output_line += "\t"
                else :
                    output_line += "\n"
            o.write(output_line)






    else :
        return "error reading input file"









    # Closing the file readers
    o.close()
    i.close()
if __name__ == "__main__":
	main()
