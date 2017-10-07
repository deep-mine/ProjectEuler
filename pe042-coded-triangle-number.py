#pe042
def wordval(word):
	score = 0
	for letter in word:
		score += (ord(letter)-64)
	return score

with open(r'C:\Users\Dibyanshu\Desktop\Project Euler\my_solutions\p042_words.txt') as w:
	wordlist = w.read().split(",")
#wordlist = [[w.split('"')] for w in words.split(",")]
#print(wordlist)
maxlen = -1
ans = ''
for word in wordlist:
	if len(word)>maxlen:
		maxlen = len(word)
		ans = word
print(ans,maxlen)
limit = 26*maxlen
print(limit)

triangle_list = []
d = 1
j = 2
while d<limit:
	triangle_list.append(d)
	d += j
	j += 1
print(triangle_list)
counter = 0
for w in wordlist:
	word = w[1:-1]
	if wordval(word) in triangle_list:
		counter += 1
		print(word,wordval(word))
print(counter)
#print(wordlist[1][1:-1],wordval(wordlist[1][1:-1]))
