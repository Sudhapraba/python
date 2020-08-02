print("To find the triangle is equilateral, scalene or isosceles")

side_a = int(input("Enter the length of side a: "))
side_b = int(input("Enter the length of side b: "))
side_c = int(input("Enter the length of side c: "))

if side_a == side_b == side_c:
  print("The triangle is equilateral")
elif side_a == side_b or side_b == side_c or side_c == side_a:
  print("The triangle is isosceles")
else:
  print("The triangle is scalene")