# NVA-Universities-Python
Scrapper that collects number of nouns, verbs and adjectives from university sites and compares them.
Selenium is used to scrap 6 webpages from 3 universities (namely NUST, LUMS and FAST).
It collects the whole text of their body tags in a string.
This string is then parsed, tokenized using nltk library and then we identify the number of nouns, verbs and adjectives on each universitie's websites.
Then a bar chart is created using matplotlib which is also uploaded here.
It shows the variation of nouns, verbs and adjectives in all three universities and gives a comparison.
Then we form a graph using networkx library of all the nouns in our text.
An edge is created between two nouns only if they lie in the same sentence.
Firstly, we print out the number of connected components by checking number of edges of each node.
Secondly, we use this graph to identify the top 10 most repeated nouns (node with most edges).
Lastly, we use djisktra's algorithm on each node to find the shortest distance between it and the node of noun "quality" (if an edge exists).
If the distance between the 2 nodes is less than 5, we print this nouns.
Finally, the program ends.
