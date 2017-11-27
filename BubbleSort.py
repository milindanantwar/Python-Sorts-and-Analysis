# Bubble Sort 
#    _____  .__.__  .__            .___ _____
#   /     \ |__|  | |__| ____    __| _//  _  \
#  /  \ /  \|  |  | |  |/    \  / __ |/  /_\  \
# /    Y    \  |  |_|  |   |  \/ /_/ /    |    \
# \____|__  /__|____/__|___|  /\____ \____|__  /
#         \/                \/      \/       \/

import itertools;

listFromUser = input("Enter list elements separated by space: \n");
listArrayStr = listFromUser.split();
listArray =  [int(x) for x in listArrayStr];
listLength = len(listArray)

for idx,valx in enumerate(listArray):
    for idy,ele in enumerate(listArray):
        if idy < listLength-1 and listArray[idy] > listArray[idy+1]:
            temp = listArray[idy]
            listArray[idy] = listArray[idy+1]
            listArray[idy+1] = temp

print(listArray)