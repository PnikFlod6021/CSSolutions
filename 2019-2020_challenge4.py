file = open('symbols.txt', 'r')
f = file.read()
def shorten_text():
    text = ""
    for i in f:
        if i.isalpha():
            text += i
    return (text.lower())
def get_hits():
    hits = {}
    for char in shorten_text():
        if char not in hits:
            hits[char] = shorten_text().count(char)
    return (hits)
def get_frequency():
    frequencies = get_hits()
    total = (sum(frequencies.values()))
    for i in frequencies:
        frequencies[i] = round((frequencies[i] / total) * 100, 1)
    return (frequencies)
def sort_dict(c):
    sorted_list = sorted(c.items(), key=lambda x:x[1], reverse=True)
    sorted_dict = dict(sorted_list)
    return (sorted_dict)
def output():
    hits = sort_dict(get_hits())
    frequencies = sort_dict(get_frequency())
    count = 0
    with open('frequencies.txt', 'w') as file:
        for key, value in hits.items():
                count+=1
                file.write(f"{count}.{key.upper()} - {value} hits at {frequencies[key]}%      |{'X' * int((frequencies[key] // 2))}\n")

output()
