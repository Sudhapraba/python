a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

temp = a
a = b
b = temp

print("Using third variable")
print("Value of a after swapping: {}".format(a))
print("Value of b after swapping: {}".format(b))

a = a + b
b = a - b
a = a - b

print("Without Using third variable")
print("Value of a after swapping: {}".format(a))
print("Value of b after swapping: {}".format(b))
