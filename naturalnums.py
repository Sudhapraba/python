number = int(input("Enter the number: "))
total = 0

for value in range(1,number + 1):
 total = total + value
   
average = total / number 
print("The total of natural number from 1 to {0} = {1}".format(number, total))
print("The average of natural number from 1 to {0} = {1}".format(number, average))