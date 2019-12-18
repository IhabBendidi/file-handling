import argparse




def main():

    # construct the argument parser and parse the arguments (input, output path )
    ap = argparse.ArgumentParser()
    ap.add_argument("-i",type=str, required=True,
        help="path to inputfile for the fifth task")
    ap.add_argument("-q",type=str, required=True,
        help="query inputed")
    args = vars(ap.parse_args())



    # Opening the input file
    i=open(args["i"], "r")

    # Retrieving the query string
    q = args["q"]

    if i.mode == 'r':
        # Reading the lines in the input file
        contents =i.readlines()

        query1 = ""
        index = 1
        bracket_clauses = []
        # Organizing the queries and substuting the between brackets clauses with corresponding keys
        if q[0] == "{":
            temp = q.split("{")[1:]
            for clause in temp:
                if len(clause.split("}")) == 2:
                    a = clause.split("}")[0]
                    query1 += str(index)
                    bracket_clauses.append({str(index) : a})
                    index += 1
                    query1 += clause.split("}")[1]
                else :
                    query1 += clause
        else :
            temp = q.split("{")
            query1 += temp[0]
            for clause in temp[1:]:
                if len(clause.split("}")) == 2:
                    a = clause.split("}")[0]
                    query1 += str(index)
                    bracket_clauses.append({str(index) : a})
                    index += 1
                    query1 += clause.split("}")[1]
                else :
                    query1 += clause

        # Organizing the BUT NOT clauses
        not_clauses = []
        index = 1
        query2 = ""
        temp = query1.split("BUT NOT")
        for tem in temp:
            t = tem.split("AND NOT")
            for a in t:
                if index == 1:
                    query2 += str(index)
                else :
                    query2 += " BUT NOT " + str(index)
                not_clauses.append({str(index) : a})
                index += 1


        # Organizing the OR clauses
        or_clauses = []
        index = 1
        for j in range(len(not_clauses)):
            query3 = ""
            temp = not_clauses[j][str(j+1)].split("OR")
            for k in range(len(temp)) :
                query3 += str(index)
                if k < len(temp) - 1 :
                    query3 += " OR "
                or_clauses.append({str(index) : temp[k]})
                index += 1
            not_clauses[j][str(j+1)] = query3


        # Organizing the AND clauses
        and_clauses = []
        index = 1
        for j in range(len(or_clauses)):
            query4 = ""
            temp = or_clauses[j][str(j+1)].split("AND")
            for k in range(len(temp)):
                query4 += str(index)
                if k < len(temp) - 1 :
                    query4 += " AND "
                and_clauses.append({str(index) : temp[k]})
                index += 1
            or_clauses[j][str(j+1)] = query4







        # Extracting the documents corresponding to the between brackets clauses


        # Computing inner clause of but not
        inner_not_clauses = []
        index = 1

        for j in range(len(bracket_clauses)):
            clause = bracket_clauses[j][str(j+1)]


            # Even inside brackets we could have different AND, OR and BUT NOT clauses that we should take in mind
            not_query = ""
            temp = clause.split("BUT NOT")
            for k in range(len(temp)) :
                t = temp[k].split("AND NOT")
                for l in range(len(t)):
                    not_query += str(index)
                    if not (l == len(t) - 1 and k == len(temp) - 1) :
                        not_query += " BUT NOT "
                    inner_not_clauses.append({str(index) : t[l]})
                    index += 1
            bracket_clauses[j][str(j+1)] = not_query




        # Computing OR inner clauses
        inner_or_clauses = []
        index = 1
        for j in range(len(inner_not_clauses)):
            clause = inner_not_clauses[j][str(j+1)]

            or_query = ""
            temp = clause.split("OR")
            for k in range(len(temp)):
                or_query += str(index)
                if k < len(temp) - 1 :
                    or_query += " OR "
                inner_or_clauses.append({str(index) : temp[k]})
                index += 1
            inner_not_clauses[j][str(j+1)] = or_query


        # Computing and inner clauses
        inner_and_clauses = []
        index = 1
        for j in range(len(inner_or_clauses)):
            clause = inner_or_clauses[j][str(j+1)]

            and_query = ""
            temp = clause.split("AND")
            for k in range(len(temp)):
                and_query += str(index)
                if k < len(temp) - 1 :
                    and_query += " AND "
                inner_and_clauses.append({str(index) : temp[k]})
                index += 1
            inner_or_clauses[j][str(j+1)] = and_query

        # Preprocessing contents of input inputfile
        sentences = []
        for document in contents :
            # Simple preprocessing
            sentence = ""
            for z in range(len(document.split("."))):
                sentence += document.split(".")[z]
            document = sentence
            sentence = ""
            for z in range(len(document.split(","))):
                sentence += document.split(",")[z]
            document = sentence
            sentence = ""
            for z in range(len(document.split("!"))):
                sentence += document.split("!")[z]
            document = sentence
            sentence = ""
            for z in range(len(document.split("?"))):
                sentence += document.split("?")[z]
            document = sentence
            sentence = ""
            for z in range(len(document.split("\n"))):
                sentence += document.split("\n")[z]
            document = sentence
            document = document.lower()
            # discarding out the document titles
            sentence = document.split("\t")[1]
            sentences.append(sentence)



        # Resolving simple basic queries
        inner_and_results = {}
        for j in range(len(inner_and_clauses)) :
            # One word queries
            if len(inner_and_clauses[j][str(j+1)].split("/")) == 1 :
                clause_word = inner_and_clauses[j][str(j+1)].strip()
                results = []
                for k in range(len(sentences)) :
                    words = sentences[k].split(" ")
                    for word in words :
                        if word == clause_word :
                            #inner_and_results.append({str(j+1) : contents[k]})
                            results.append(contents[k])
                            break
                inner_and_results[str(j+1)] = results
            #proximity queries ( clause_word / proximity anchor)
            else :
                proximity = int(inner_and_clauses[j][str(j+1)].split("/")[1].split(" ")[0])
                anchor = inner_and_clauses[j][str(j+1)].split("/")[1].split(" ")[1].strip()
                clause_word = inner_and_clauses[j][str(j+1)].split("/")[0].strip()
                results = []
                for k in range(len(sentences)) :
                    words = sentences[k].split(" ")
                    for l in range(len(words)) :
                        if words[l] == anchor :
                            for m in range(min(l-proximity,0),max(l+proximity-1,len(words))):

                                if words[m] == clause_word :
                                    results.append(contents[k])
                                    break
                inner_and_results[str(j+1)] = results




        #print(inner_or_clauses)
        #print(inner_and_results)
        # Resolving inner OR queries
        inner_or_results = {}
        for j in range(len(inner_or_clauses)) :
            query = inner_or_clauses[j][str(j+1)]
            #print(query)

            clause_s = query.split("AND")
            tempa = []
            for k in range(len(clause_s)) :
                clause_s[k] = clause_s[k].strip()

                tempa.append(inner_and_results[clause_s[k]])

            # finding intersection between the clauses
            if len(tempa) == 1 :
                intersection = set(tempa[0])
            else :
                intersection = set(tempa[0]) & set(tempa[1])
                for b in range(1,len(tempa)):
                    intersection = set(intersection) & set(tempa[b])
            #print(intersection)
            inner_or_results[str(j+1)] = list(intersection)





        # Resolving inner NOT clause_s
        #print(inner_not_clauses)
        #print(inner_or_results)
        inner_not_results = {}
        for j in range(len(inner_not_clauses)) :
            query = inner_not_clauses[j][str(j+1)]
            #print(query)

            clause_s = query.split("OR")
            tempa = []
            for k in range(len(clause_s)) :
                clause_s[k] = clause_s[k].strip()

                tempa.append(inner_or_results[clause_s[k]])

            # finding intersection between the clauses
            if len(tempa) == 1 :
                union = set(tempa[0])
            else :
                union = set(tempa[0]) | set(tempa[1])
                for b in range(1,len(tempa)):
                    union = set(union) | set(tempa[b])
            #print(intersection)
            inner_not_results[str(j+1)] = list(union)

        #print(inner_not_results)
        #print(bracket_clauses)


        # Resolving brackets

        bracket_results = {}
        for j in range(len(bracket_clauses)) :
            query = bracket_clauses[j][str(j+1)]
            #print(query)

            clause_s = query.split("BUT NOT")
            tempa = []
            for k in range(len(clause_s)) :
                clause_s[k] = clause_s[k].strip()

                tempa.append(inner_not_results[clause_s[k]])

            # finding intersection between the clauses
            if len(tempa) == 1 :
                substraction = set(tempa[0])
            else :
                substraction = set(tempa[0]) - set(tempa[1])
                for b in range(1,len(tempa)):
                    substraction = set(substraction) - set(tempa[b])
            #print(intersection)
            bracket_results[str(j+1)] = list(substraction)

        #print(bracket_results)

        # Resolving  queries outside of brackets
        and_results = {}
        for j in range(len(and_clauses)) :
            # One word queries
            if and_clauses[j][str(j+1)].strip().isnumeric():
                and_results[str(j+1)] = bracket_results[and_clauses[j][str(j+1)].strip()]

            elif len(and_clauses[j][str(j+1)].split("/")) == 1 :
                clause_word = and_clauses[j][str(j+1)].strip()
                results = []
                for k in range(len(sentences)) :
                    words = sentences[k].split(" ")
                    for word in words :
                        if word == clause_word :
                            #inner_and_results.append({str(j+1) : contents[k]})
                            results.append(contents[k])
                            break
                and_results[str(j+1)] = results
            #proximity queries ( clause_word / proximity anchor)
            else :
                proximity = int(and_clauses[j][str(j+1)].split("/")[1].split(" ")[0])
                anchor = and_clauses[j][str(j+1)].split("/")[1].split(" ")[1].strip()
                clause_word = and_clauses[j][str(j+1)].split("/")[0].strip()
                results = []
                for k in range(len(sentences)) :
                    words = sentences[k].split(" ")
                    for l in range(len(words)) :
                        if words[l] == anchor :
                            for m in range(min(l-proximity,0),max(l+proximity-1,len(words))):

                                if words[m] == clause_word :
                                    results.append(contents[k])
                                    break
                and_results[str(j+1)] = results

        #print(and_clauses)
        #print(and_results)

        # Resolving And queries outside of brackets
        or_results = {}
        for j in range(len(or_clauses)) :
            query = or_clauses[j][str(j+1)]
            #print(query)

            clause_s = query.split("AND")
            tempa = []
            for k in range(len(clause_s)) :
                clause_s[k] = clause_s[k].strip()

                tempa.append(and_results[clause_s[k]])

            # finding intersection between the clauses
            if len(tempa) == 1 :
                intersection = set(tempa[0])
            else :
                intersection = set(tempa[0]) & set(tempa[1])
                for b in range(1,len(tempa)):
                    intersection = set(intersection) & set(tempa[b])
            #print(intersection)
            or_results[str(j+1)] = list(intersection)

        #print(or_clauses)
        #print(or_results)





        # Resolving or outside of brackets
        not_results = {}
        for j in range(len(not_clauses)) :
            query = not_clauses[j][str(j+1)]
            #print(query)

            clause_s = query.split("OR")
            tempa = []
            for k in range(len(clause_s)) :
                clause_s[k] = clause_s[k].strip()

                tempa.append(or_results[clause_s[k]])

            # finding intersection between the clauses
            if len(tempa) == 1 :
                union = set(tempa[0])
            else :
                union = set(tempa[0]) | set(tempa[1])
                for b in range(1,len(tempa)):
                    union = set(union) | set(tempa[b])
            #print(intersection)
            not_results[str(j+1)] = list(union)

        #print(not_clauses)
        #print(not_results)


        #print(query2)
        # Final results
        final_results = {}
        for j in range(len([query2])) :
            query = query2
            #print(query)

            clause_s = query.split("BUT NOT")
            tempa = []
            for k in range(len(clause_s)) :
                clause_s[k] = clause_s[k].strip()

                tempa.append(not_results[clause_s[k]])

            # finding intersection between the clauses
            if len(tempa) == 1 :
                substraction = set(tempa[0])
            else :
                substraction = set(tempa[0]) - set(tempa[1])
                for b in range(1,len(tempa)):
                    substraction = set(substraction) - set(tempa[b])
            #print(intersection)
            final_results[str(j+1)] = list(substraction)








        # Outputing the results to the console
        for sentence in final_results["1"]:
            print(sentence)




































    else :
        return "error reading input file"









    # Closing the file readers
    i.close()
if __name__ == "__main__":
	main()
