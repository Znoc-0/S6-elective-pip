

f = open("nums.txt", "r")
feven = open("even.txt", "w")
fodd = open("odd.txt", "w")

even, odd = "", ""

nums = f.read()
print(nums)
nums = nums.split(" ")

for num in nums:
    if int(num)%2==0:
        even += num + " "
    else:
        odd += num + " "
        
feven.write(even)
fodd.write(odd)

f.close()
even.close()
odd.close()