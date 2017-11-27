# Factoarial of a number
#    _____  .__.__  .__            .___ _____
#   /     \ |__|  | |__| ____    __| _//  _  \
#  /  \ /  \|  |  | |  |/    \  / __ |/  /_\  \
# /    Y    \  |  |_|  |   |  \/ /_/ /    |    \
# \____|__  /__|____/__|___|  /\____ \____|__  /
#         \/                \/      \/       \/

def factorial(num):
    if num == 0:
        return 1;
    else:
        return num * factorial(num-1);

numFromUser = input("Enter element for factorial: \n");
numForFactorial = int(numFromUser);
print("Factorial of number is : "+str(factorial(numForFactorial)));