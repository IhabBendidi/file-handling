# Context
This is a training project to find similarities between documents, and creating a query language for searching for documents in a document database tha resolve specific characteristics, through processing, manipulating and data mining text data. The requirement of the exercice is to use the Python language, without using any single external library, and implementing from scratch all parts. you can find the full details of the exercice [here](https://github.com/IhabBendidi/file-handling/blob/master/_/IRWS2019.pdf).



# Task 1

### Purpose 
The goal of this task is to write a script, without usage of any external library, that process basic text files containing numerous documents, and saves their output. This processing should consider punctuation, lower-casting, numbers, stop word removal and stemming.

### Implementation
The command to launch the script for the task 1 is  :

```  python3 task1.py -i "input1.txt" -o "output.txt" -s "stopword_list.txt"  ```

You can provide your own stopword lists beside the one already in the project.
The output is written to the file path you would give, if file already exists, or create a new file if it doesnt.
The input file should necessarily have inside a title for each document, followed by a tab.

To test the stemming script against the example given on the [link](https://tartarus.org/martin/PorterStemmer/index.html) provided on the instruction file, you can test it through the following script in the "_" folder :

```  python3 teststemmer.py -i "voc.txt" -s "stopword_list.txt"  ```

The input voc.txt was provided by the website Tartarus and is in the current folder
The output of the script would be in the command line, and could be compared to the results provided in the website for accuracy (100%)
The results provided by the website can be found in [here](https://tartarus.org/martin/PorterStemmer/output.txt)



# Task 2

### Purpose
The goal of this task is to read document files that have been already preprocessed, and create, without usage of any external library, an inverted index of the word in them.

### Implementation
The task 2 involves creating a script that creates an inverted index. To run it against the results of the previous task, this is the command to launch :


```  python3 task2.py -i "input2.txt" -o "output.txt"  ```

The output is written to the file path you would give, if file already exists, or create a new file if it doesnt.


# Task 3

### Purpose
The goal of this task is to read an inverted index, without usage of any external library, and transform it into the TF-IDF matrix containing the TF-IDF score of each term

### Implementation
This task is about creating the TF-IDF matrix. The formulas used for computing are :

IDF(t) = log_e(Total number of documents / Number of documents with term t in it)

TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)

TF-IDF(t) = TF(t) * IDF(t)

The command to launch the script correctly is :

```  python3 task3.py -i input3.txt -o output.txt  ```

The output is written to the file path you would give, if file already exists, or create a new file if it doesnt.

# Task 4

### Purpose
The purpose of this task is to compute, without usage of any external library, the cosine similarity between two documents, after reading the TF-IDF matrix of scores.

### Implementation
This task is about computing the cosine similarity between two documents, using the TF-IDF weight matrix previously created. The path to the input file is the previously created matrix.

The command to launch the script is :

```  python3 task4.py -i input4.txt -a D4 -b D5  ```

With the flag ``-a`` for the first document, and the ``-b`` for the second document

The output is returned in the console.

# Task 5

### Purpose
The purpose of this task is creating, without usage of any external library, an unified complex proximity query language for finding documents that contain specific content, and resolving successfully those queries. You can find [here](https://github.com/IhabBendidi/file-handling/blob/master/_/IRWS2019.pdf) more details about the specifics of the query language implemented in this task.

### Implementation
This task is about resolving queries about the documents, under a certain order and priorities.

The ``-i`` flag is for the input file, of normal documents ( the first input file used).

The ``-q`` flag is for the string of the query being used. Priority has been given to queries between brackets, then to AND, then OR, Then BUT NOT/AND NOT.

The queries inside the brackets have also been resolved using the same order of priority.

If you use another input file, keep it in the format (title \t document) of the original file

```  python3 task5.py -i input1.txt -q "{first /5 documents AND documents} AND is OR insist BUT NOT others"  ```

The documents resolving the query are returned as output in the console.
