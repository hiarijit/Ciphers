alphabet = "abcdefghijklmnopqrstuvwxyz"
x = input("Enter the ciphertext(in capital letters) to be broken : ")
print()
for i in range(26):
    string = ""
    for j in range(len(x)):
        for k in range(len(alphabet)):
            if alphabet[k] == x[j].lower():
                string += alphabet[(k+i) % 26]
                break
    print(string)

