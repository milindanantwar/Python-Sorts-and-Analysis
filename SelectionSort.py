# Selection Sort
#    _____  .__.__  .__            .___ _____
#   /     \ |__|  | |__| ____    __| _//  _  \
#  /  \ /  \|  |  | |  |/    \  / __ |/  /_\  \
# /    Y    \  |  |_|  |   |  \/ /_/ /    |    \
# \____|__  /__|____/__|___|  /\____ \____|__  /
#         \/                \/      \/       \/

import itertools;

listFromUser = input("Enter list elements separated by space: \n");
listArrayStr = listFromUser.split();
listArray = [int(x) for x in listArrayStr];
listLength = len(listArray)

for idx in range(listLength):
    currentIndex = idx;
    minPosIndex = currentIndex;
    for idy in range(currentIndex, listLength):
        if listArray[minPosIndex] > listArray[idy]:
            minPosIndex = idy;

    if minPosIndex != currentIndex:
        temp = listArray[minPosIndex];
        listArray[minPosIndex] = listArray[currentIndex];
        listArray[currentIndex] = temp;


print(listArray);