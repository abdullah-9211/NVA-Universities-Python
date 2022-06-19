"""=============ABDULLAH UMAR, RIMSHA IFTIKHAR, NOMAN MAQSOOD AND HASSAAN ANWAR===========
================STUDENT NAME: ABDULLAH UMAR=====================================
================TEACHER NAME: MUHAMMAD ARSHAD ISLAM============================="""


#===========USER DEFINED FUNCTIONS==============#

def isSymbol(c) -> bool:
    if (c >= '0' and c <= '9') or (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
        return False
    return True


import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import networkx as nx
from matplotlib import pyplot as plt
import nltk
from nltk.probability import FreqDist
import random

PATH = r"D:\Uni Stuff\Discrete structures\Project Phase 2\chromedriver.exe"

driver = webdriver.Chrome(PATH)

#getting data from fast nuces site

fast_links = ["http://nu.edu.pk/", "http://nu.edu.pk/University/Foundation", "http://nu.edu.pk/Program/BS(CS)", "http://nu.edu.pk/Program/MS(CS)", "http://nu.edu.pk/Program/PhD(CS)"]
fast_str = ""

for i in range(5):
    driver.get(fast_links[i])
    temp = driver.find_element_by_tag_name("body")
    fast_str += temp.text

#getting data from lums site

lums_links = ["https://lums.edu.pk/aboutlums", "https://lums.edu.pk/", "https://sbasse.lums.edu.pk/", "https://sbasse.lums.edu.pk/department-of-computer-science", "https://sbasse.lums.edu.pk/sbasse-undergraduate-education"]
lums_str = ""


for i in range(5):
    driver.get(lums_links[i])
    temp = driver.find_element_by_tag_name("body")
    lums_str += temp.text

#getting data from nust site

nust_links = ["https://qa.nust.edu.pk/", "https://nust.edu.pk/", "https://seecs.nust.edu.pk/", "https://nbs.nust.edu.pk/", "https://nust.edu.pk/about-us"]
nust_str = ""



for i in range(5):
    driver.get(nust_links[i])
    temp = driver.find_element_by_tag_name("body")
    nust_str += temp.text

#quitting scrapper
driver.quit()

#tokenizing fast data

fast_tokens = nltk.word_tokenize(fast_str)

fast_tags = nltk.pos_tag(fast_tokens)
f_nouns = []
f_verb = []
f_adj = []

#tokenizing lums data

lums_tokens = nltk.word_tokenize(lums_str)

lums_tags = nltk.pos_tag(lums_tokens)
l_nouns = []
l_verb = []
l_adj = []

#tokenizing nust data

nust_tokens = nltk.word_tokenize(nust_str)

nust_tags = nltk.pos_tag(nust_tokens)
n_nouns = []
n_verb = []
n_adj = []


#Identifying nouns, verbs and adjectives from fast site

for word,pos in fast_tags:
    if pos == "NN" or pos == "NNS" or pos == "NNP" or pos == "NNPS":
        f_nouns.append(word)
    elif pos == "VB" or pos == "VBD" or pos == "VBG" or pos == "VBN" or pos == "VBP" or pos == "VBZ":
        f_verb.append(word)
    elif pos == "JJ" or pos == "JJS" or pos == "JJK":
        f_adj.append(word)

#Identifying nouns, verbs and adjectives from lums site

for word,pos in lums_tags:
    if pos == "NN" or pos == "NNS" or pos == "NNP" or pos == "NNPS":
        l_nouns.append(word)
    elif pos == "VB" or pos == "VBD" or pos == "VBG" or pos == "VBN" or pos == "VBP" or pos == "VBZ":
        l_verb.append(word)
    elif pos == "JJ" or pos == "JJS" or pos == "JJK":
        l_adj.append(word)

#Identifying nouns, verbs and adjectives from nust site

for word,pos in nust_tags:
    if pos == "NN" or pos == "NNS" or pos == "NNP" or pos == "NNPS":
        n_nouns.append(word)
    elif pos == "VB" or pos == "VBD" or pos == "VBG" or pos == "VBN" or pos == "VBP" or pos == "VBZ":
        n_verb.append(word)
    elif pos == "JJ" or pos == "JJS" or pos == "JJK":
        n_adj.append(word)


#getting frequencies of nouns, verbs and adjectives from fast site data set

fast_n_num = nltk.FreqDist(f_nouns)
fast_n_sum = 0

for i in fast_n_num.values():
    fast_n_sum += i


fast_v_num = nltk.FreqDist(f_verb)
fast_v_sum = 0

for i in fast_v_num.values():
    fast_v_sum += i


fast_a_num = nltk.FreqDist(f_adj)
fast_a_sum = 0

for i in fast_a_num.values():
    fast_a_sum += i


#getting frequencies of nouns, verbs and adjectives from lums site data set

lums_n_num = nltk.FreqDist(l_nouns)
lums_n_sum = 0

for i in lums_n_num.values():
    lums_n_sum += i


lums_v_num = nltk.FreqDist(l_verb)
lums_v_sum = 0

for i in lums_v_num.values():
    lums_v_sum += i


lums_a_num = nltk.FreqDist(l_adj)
lums_a_sum = 0

for i in lums_a_num.values():
    lums_a_sum += i


#getting frequencies of nouns, verbs and adjectives from nust site data set

nust_n_num = nltk.FreqDist(n_nouns)
nust_n_sum = 0

for i in nust_n_num.values():
    nust_n_sum += i


nust_v_num = nltk.FreqDist(n_verb)
nust_v_sum = 0

for i in nust_v_num.values():
    nust_v_sum += i


nust_a_num = nltk.FreqDist(n_adj)
nust_a_sum = 0

for i in nust_a_num.values():
    nust_a_sum += i

#drawing bar chart to show difference in number of nouns, verbs and adjectives between the two websites

groups = 3
d1 = (fast_n_sum, fast_v_sum, fast_a_sum)
d2 = (lums_n_sum, lums_v_sum, lums_a_sum)
d3 = (nust_n_sum, nust_v_sum, nust_a_sum)

fig,ax = plt.subplots()
index = np.arange(groups)
bar = 0.25

plt.bar(index, d1, bar, color = 'b', label = 'Nouns')
plt.bar(index + bar, d2, bar, color = 'g', label = 'Verbs')
plt.bar(index + bar + bar, d3, bar, color = 'r', label = 'Adjectives')


plt.xlabel("Parts of Speech")
plt.ylabel("Frequency")
plt.xticks(index+bar,('Nouns','Verbs','Adjectives'))
plt.legend(["FAST","LUMS","NUST"])

plt.tight_layout()
plt.show()

#collecting all the nouns in one list

all_nouns = []

for i in f_nouns:
    all_nouns.append(i)

for j in l_nouns:
    all_nouns.append(j)

for k in n_nouns:
    all_nouns.append(k)

#Collecting all the text in string and then tokenizing for graph formation

all_str = ""

all_str += (fast_str + lums_str + nust_str)

all_token = nltk.word_tokenize(all_str)


#Graph Formation

Noun_Graph = nx.DiGraph()

for n in all_nouns:
    Noun_Graph.add_node(n)

noun1 = ""
noun2 = ""

#adds edge only between the nouns which are in the same sentence

for c in range(len(all_token)):

    if (all_token[c] in all_nouns) and (noun1 == "") and not (isSymbol(all_token[c][0])):
        noun1 = all_token[c]
    elif (all_token[c] in all_nouns) and (noun2 == "") and not (isSymbol(all_token[c][0])):
        noun2 = all_token[c]

    if (noun1 != "") and (noun2 != ""):
        Noun_Graph.add_edge(noun1,noun2)
        noun1 = ""
        noun2 = ""

    if (all_token[c] == '.') or (all_token[c] == '?') or (all_token[c] == '!') or (all_token[c] == '\n'):
        noun1 = ""
        noun2 = ""


#Finding the degree of each node and outputting number of connected components

connected = 0

for val in Noun_Graph.degree():
    if (val[1] > 0):
        connected += 1

print()
print()
print("=========================CONNECTED COMPONENTS=======================")
print()

print("Total Nouns are " + str(len(all_nouns)))
print()

print("Connected components in the graph are " + str(connected) + " Nouns")


#Printing top 10 nouns based on degree of node

print()
print()

print("=========================TOP 10 NOUNS=========================")
print()

sorted_deg = sorted(Noun_Graph.degree(), key=lambda x:x[1], reverse=True)

print()
print()

for i in range(10):
    print(str(i+1) + ". " + str(sorted_deg[i][0]) + " with degree: " + str(sorted_deg[i][1]))


print()
print()

#Finding all the nouns with distance <5 from the noun "quality"

print("===============DISTANCE < 5 FROM *QUALITY*=======================")
print()
print()


count = 1

for i in all_nouns:
    if nx.has_path(Noun_Graph, source=i, target="quality"):
        if (nx.shortest_path_length(Noun_Graph, source=i, target="quality", weight=None, method="dijkstra")) < 5:
            print(str(count) + ". " + i)
            count += 1