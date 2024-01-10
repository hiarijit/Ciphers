alphabet = "abcdefghijklmnopqrstuvwxyz"
x = input("Enter the ciphertext (in capital letters) to be decrypted : ")
shift = int(input("Enter the key (shift) to decrypt the ciphertext (0-25): "))
print()
plaintext = ""
for j in range(len(x)):
    for k in range(len(alphabet)):
        if alphabet[k] == x[j].lower():
            plaintext += alphabet[(k-shift) % 26]
            break
print("The corresponding ciphertext is : " + plaintext)