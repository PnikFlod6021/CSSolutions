digits = {
    'O' : 0,
    'L': 1,
    'Z': 2,
    'E': 3,
    'A': 4,
    'S': 5,
    'T': 7,
    'G': 9
}

x = input("Phrase")
z = x.upper()
for i in range(len(z)):
    if z[i] in digits:
        z = z.replace(z[i], str(digits[z[i]]))
        
print(z)
