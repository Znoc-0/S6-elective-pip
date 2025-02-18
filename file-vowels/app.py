

f = open("data.txt", "r")
fw = open("write.txt", "w")

text = f.read()
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
newtext = text

for i in text:
    if i in vowels:
        newtext = newtext.replace(i, "#")

fw.write(newtext)

f.close()
fw.close()