
n = int(input("Enter the number : "))
rev = 0
number = n
while(n != 0):
  rem = n % 10
  rev = rev * 10 + rem
  n = int(n / 10)
if(number == rev):
  print("Palindrome")
else:
  print("Not a Palindrome")
