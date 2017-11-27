# Fibonacci Series
#    _____  .__.__  .__            .___ _____
#   /     \ |__|  | |__| ____    __| _//  _  \
#  /  \ /  \|  |  | |  |/    \  / __ |/  /_\  \
# /    Y    \  |  |_|  |   |  \/ /_/ /    |    \
# \____|__  /__|____/__|___|  /\____ \____|__  /
#         \/                \/      \/       \/

num0,num1 = 0,1;
#num0 = 0;
#num1 = 1;
#def fibonacci(num):


numFromUser = input("Enter a number: \n");
numForFib = int(numFromUser);
strForPrint = "Fibonacci Series %s %s" % (num0, num1);

while(num1+num0 < numForFib):
    nunm = num1 + num0
    strForPrint += " " + str(nunm);
    num0 = num1;
    num1 = nunm;

print(strForPrint)