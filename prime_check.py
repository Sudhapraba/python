input = int(input("Enter a number: "))
if input > 1:
  for i in range(2,input):
    if (input % i) == 0:
      print(input,"is not a prime number")
      break
  else:
      print(input,"is a prime number")
else:
 print(input,"is not a prime number")
  