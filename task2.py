import argparse



def main():

    # construct the argument parser and parse the arguments (input, output path )
    ap = argparse.ArgumentParser()
    ap.add_argument("-i",type=str, required=True,
        help="path to inputfile for the second task")
    ap.add_argument("-o",type=str, required=True,
        help="path to output file if it exists, if not, it will be created")
    args = vars(ap.parse_args())

    # Opening the input file
    i=open(args["i"], "r")
    if i.mode == 'r':
        # Reading the lines in the input file
        contents =i.readlines()
        raw_index = []
        # Deleting duplicates from the same documents
        for line in contents :
            title,document = line.split("\t")
            words = document.split(" ")
            raw_index.append([words[0],title])
            for j in range(1,len(words)) :
                exist = False
                for k in range(j-1):
                    if words[k] == words[j]:
                        exist = True
                        break
                if not exist :
                    words[j] = words[j].split("\n")[0]
                    raw_index.append([words[j],title])
        # Organizing the inverted index
        final_output = []
        final_output.append(raw_index[0])
        for j in range(1,len(raw_index)):
            exists = False
            for k in range(len(final_output)):
                if raw_index[j][0] == final_output[k][0]:
                    final_output[k].append(raw_index[j][1])
                    exists = True
                    break
            if not exists :
                final_output.append(raw_index[j])
    else :
        return "error reading input file"



    # Opening the output file ( or creating it if it doesnt exist)
    o=open(args["o"], "w+")

    for line in final_output :
        inverted_index = line[0] + "\t"
        for j in range(1,len(line)):
            inverted_index += line[j]
            if j<len(line)-1 :
                inverted_index += "\t"
        # Writing the outputs in the output file
        o.write(inverted_index + "\n")

    # Closing the file readers
    o.close()
    i.close()










if __name__ == "__main__":
	main()
