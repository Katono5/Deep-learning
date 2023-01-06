def insertion(list1):
    n = len(list1)
    for i in range(1, n):
        j = i - 1
        key = list1[i]
        while (j>=0 and list1[j] > key):
            list1[j+1] = list1[j]
            j -= 1
        list1[j+1] = key
    print(list1)

list2 = [55, 22, 44, 11, 33]
insertion(list2)

import pandas as pd
import numpy as np
list2=[55, 22, 44, 11, 33]
def insert_sort(list1):
    newls=np.append(0,list1)
    for i in range(2,len(newls)):
        if newls[i]<newls[i-1]:
            newls[0]=newls[i]
            j=i
            while newls[j-1]>newls[0]:
                newls[j]=newls[j-1]
                j=j-1

            newls[j]=newls[0]
    return newls[1:len(newls)]

print(insert_sort(list2))

def selection(list1):
    n = len(list1)
    for i in range(n-1):
        min = i
        for j in range(min, n):
            if list1[min] > list1[j]:
                min = j
        list1[min], list1[i] = list1[i], list1[min]
    return list1

list2 = [49, 27, 65, 76, 13, 97]
print(selection(list2))