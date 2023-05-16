#Python program to find the largest element of the array
lst = []
num = int(input("Enter the size of the array: "))
print("Enter array elements: ")
for n in range(num):
  numbers = int(input())
  lst.append(numbers)
large = lst[0]
for n in range(num):
  if(lst[n] > large):
    large = lst[n]
print("The largest element of the given list is:", large)