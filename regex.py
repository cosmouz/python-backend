import re

word1 = "темир"
word2 = "томир"
word3 = "тулпор"

andoza = "^т....р"

print(re.match(andoza, word1))
print(re.match(andoza, word2))
print(re.match(andoza, word3))