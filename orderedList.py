List = [1, 2, 4, 3, 8, 6, 5]
print("\nList with the use of Numbers: ")
List.sort()
print(List)

print("Checking if number exists in list")

# number of times element exists in list
number = int(input("enter number:"))
if number in List:
    print("exist")
else:
    print("not exist")

print(List)
List.remove(number)
print("\nList after removing a specific element: ")
print(List)
