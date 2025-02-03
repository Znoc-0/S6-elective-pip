n = int(input("Enter number of elements : "))
list_a = [int(input()) for i in range(0, n)]
print("List: ",list_a)


n2 = int(input("Enter number of elements in list 2: "))

list_b = [int(input()) for i in range(0, n2)]
print("List 2: ",list_b)

common = [i for i in list_a if i in list_b]

print("Common elements: ",common)