# word freqyency
paragraph = "Hello my name is mohana and my bro is also mohana"
words = paragraph.lower().split()
frequency = {}
for word in words:
    words_clean = word.strip('.,!?()[]{}":;')

    if words_clean in frequency:
        frequency[words_clean] += 1
    else:
        frequency[words_clean] = 1

for index,item in enumerate(frequency):
    print(f"{item}==>{index}")