a= [3,5,7,2,0,1,4,6,8,9]


first = second = third = 0

for i in a:
    if i > first:
        third = second
        second = first
        first = i
    elif i > second:
        third = second
        second = i
    elif i > third:
        third = i

print("First:", first)
print("Second:", second)
print("Third:", third)