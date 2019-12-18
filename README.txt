# Task 1
The command to launch the script for the task 1 is (has to be launched through the command line in this folder, or provide complete paths for each file) :

```  python3 task1.py -i "input1.txt" -o "output.txt" -s "stopword_list.txt"  ```

You can provide your own stopword lists beside the one already in the project.
The output is written to the file path you would give, if file already exists, or create a new file if it doesnt.
The input file should necessarily have inside a title for each document, followed by a tab.

To test the stemming script against the example given on the link provided on the instruction file
(https://tartarus.org/martin/PorterStemmer/index.html), you can test it through the following script in the "_" folder :

```  python3 teststemmer.py -i "voc.txt" -s "stopword_list.txt"  ```

The input voc.txt was provided by the website Tartarus and is in the current folder
The output of the script would be in the command line, and could be compared to the results provided in the website for accuracy (100%)
The results provided by the website can be found in https://tartarus.org/martin/PorterStemmer/output.txt



# Task 2
 The task 2 involves creating a script that creates an inverted index. To run it against the results of the previous task, this is the command to launch :


```  python3 task2.py -i "input2.txt" -o "output.txt"  ```

The output is written to the file path you would give, if file already exists, or create a new file if it doesnt.


# Task 3

This task is about creating the TF-IDF matrix. The formulas used for computing are :

IDF(t) = log_e(Total number of documents / Number of documents with term t in it)

TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)

TF-IDF(t) = TF(t) * IDF(t)

The command to launch the script correctly is :

```  python3 task3.py -i input3.txt -o output.txt  ```

The output is written to the file path you would give, if file already exists, or create a new file if it doesnt.

# Task 4

This task is about computing the cosine similarity between two documents, using the TF-IDF weight matrix previously created. The path to the input file is the previously created matrix.

The command to launch the script is :

```  python3 task4.py -i input4.txt -a D4 -b D5  ```

With the flag ``-a`` for the first document, and the ``-b`` for the second document

The output is returned in the console.

# Task 5

This task is about resolving queries about the documents, under a certain order and priorities.

The ``-i`` flag is for the input file, of normal documents ( the first input file used).

The ``-q`` flag is for the string of the query being used. Priority has been given to queries between brackets, then to AND, then OR, Then BUT NOT/AND NOT.

The queries inside the brackets have also been resolved using the same order of priority.

If you use another input file, keep it in the format (title \t document) of the original file

```  python3 task5.py -i input1.txt -q "{first /5 documents AND documents} AND is OR insist BUT NOT others"  ```

The documents resolving the query are returned as output in the console.
