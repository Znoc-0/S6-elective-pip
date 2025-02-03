
a=[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    a.append(int(input()))

print("a = ",a)

check = int(input("enter the number to check"))

new_list = [ num for num in a if num < check]

print("Numbers less than ",check," are ",new_list)

