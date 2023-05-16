x = int(input("Enter the value for x :"))
y = int(input("Enter the value for y :"))
z = int(input("Enter the value for z :"))
#comparing integer ‘a’ with other two integer
if x<=y and x<=z:
	print("a is smallest")
#comparing integer ‘b’ with other two integer
elif y<=x and y<=z:
	print("b is smallest")
#comparing integer ‘c’ with other two integer
elif z<=x and z<=y:
	print("c is smallest")