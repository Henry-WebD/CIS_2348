#Henry Saravia, PSID: 1853318

wordlist = list(input().split(" "))

word_frequency = []

for x in wordlist:
    word_frequency.append(wordlist.count(x))

for i in range(len(wordlist)):
    print(wordlist[i], word_frequency[i])
