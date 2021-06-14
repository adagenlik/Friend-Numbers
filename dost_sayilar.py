# A and B are two positive integers
# The sum of the positive divisors of A excluding itself is B and
# If the sum of the positive divisors of B excluding itself is A, then these are friendly numbers.

numberA=int(input("Write your first number:"))
numberB=int(input("Write your second number:"))

#first I'll find the positive divisors excluding itself
totalA=0
totalB=0 

for i in range(1,numberA):
    if(numberA%i == 0):
        totalA +=i
        

for i in range(1,numberB):
    if(numberB%i == 0):
        totalB +=i
        
if(numberA == totalB):
    if numberB == totalA:
        print("They are friendly numbers")
else:
    print("They are not friendly numbers")

