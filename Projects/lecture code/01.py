# Numeric expressions
2022
2000 + 22
1 + 2 + 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Functions
abs(-2)

# Values
"Go Bears"

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:25]
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

# Sets
words = set(text)
len(words)

# Combinations
'draw'
'draw'[0]
{w[0] for w in words}

# Data
'draw'[::-1]
{w for w in words if w == w[::-1] and len(w)>4}
{w for w in words if w[::-1] in words and len(w) == 4}
{w for w in words if w[::-1] in words and len(w) > 6}
