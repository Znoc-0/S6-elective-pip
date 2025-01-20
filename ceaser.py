
while True:
    ch = int(input("---MENU---\n 1. Encryption\n 2. Decryption\n 3. Exit\nEnter ur choice: "))
    if ch == 1:
        text = input("Enter text to encrypt: ")
        key = int(input("Enter key: "))
        encrypted = ""
        for letter in text:
            ascii = ord(letter)
            if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
                ascii += key
            if 'A' <= letter <= 'Z' and ascii > 90:
                ascii -= 26
            elif 'a' <= letter <= 'z' and ascii > 122:
                ascii -= 26
        
            encrypted += chr(ascii)
    
        print(encrypted + "\n")
    elif ch == 2:
        text = input("Enter text to decrypt: ")
        key = int(input("Enter key: "))
        decrypted = ""
        for letter in text:
            ascii = ord(letter)
            if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
                ascii -= key
            if 'A' <= letter <= 'Z' and ascii < 65:
                ascii += 26
            elif 'a' <= letter <= 'z' and ascii < 97:
                ascii += 26
        
            decrypted += chr(ascii)
        print(decrypted)
    elif ch == 3:
        break