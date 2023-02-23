values = {
    "o": 0,
    "l": 1,
    "z": 2,
    "e": 3,
    "a": 4,
    "s": 5,
    "t": 7,
    "g": 9
}
sentence = input("Entered Phrase: ")
for char in sentence:
    if char in values:
        char.lower()
        sentence = sentence.replace(char, str(values[char]))
print(f"1337 Phrase:    {sentence}")
