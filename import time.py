import time
import os, psutil
import sys
import pandas as pd

import csv
li=[]
li1=[]
count=0

dicta = pd.read_csv("C:\\Users\\vivekjuki\\OneDrive\\Desktop\\code\\french_dictionary.csv", header=None )
dicta.index = dicta[0]
dicta.drop(labels=[0], axis=1, inplace=True)
dicta.index.name = "Engish"
dicta.columns = ["Frech"]
dicta.newcolumns="fre"

fo=open("C:\\Users\\vivekjuki\\OneDrive\\Desktop\\code\\t8.shakespeare.translated.txt","a")
with open("C:\\Users\\vivekjuki\\OneDrive\\Desktop\\code\\t8.shakespeare.txt", "r") as files:

    for line in files.readlines():
            li1.append(line)
le=len(li1)
with open("C:\\Users\\vivekjuki\\OneDrive\\Desktop\\code\\find_words.txt", "r") as file:
    for line in file:
        for word in line.split():
            li.append(word)
temp={wo:0 for wo in li}
le1=len(li)
starttime=time.time()
for i in range(0,le):
    word=li1[i].split()
    for j in range(len(word)):
        count=0
        if(word[j].lower() in li):
            temp[word[j].lower()]=temp.get(word[j].lower())+1
            word[j]=dicta.loc[word[j].lower()].values[0]
    li1[i]=" ".join(word)
for i in range(le):
    li1[i]=li1[i]+"\n"

fo.writelines(li1)
with open('C:\\Users\\vivekjuki\\OneDrive\\Desktop\\code\\frequency.csv', 'w', newline="") as f:
    

    for key, value in temp.items():
        f.write(str(key)+","+str(dicta.loc[key].values[0])+","+str(value)+"\n")


endtime=time.time()
a=endtime-starttime

m=(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
tm=sys.getsizeof(li)+sys.getsizeof(li1)+sys.getsizeof(temp)+sys.getsizeof(dicta)
print("Time Taken To Process-->",a)
print("Memory Processed-->",m)
