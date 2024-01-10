alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = input("Enter the plaintext (in small letters) to be encrypted : ")
shift = int(input("Enter the key (shift) to encrypt the plaintext (0-25): "))
print()
ciphertext = ""
for j in range(len(x)):
    for k in range(len(alphabet)):
        if alphabet[k] == x[j].upper():
            ciphertext += alphabet[(k+shift) % 26]
            break
print("The corresponding ciphertext is : " + ciphertext)


