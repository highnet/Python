vowels = ['a', 'e', 'i', 'o', 'u']
found = {}
for letter in vowels:
    found[letter] = 0
print (found)
word = input("Provide a word to search for vowels: ")
for char in word:
    if char in vowels:
        found[char] += 1
print (found)

for k, v in sorted(found.items()):
    print (k, 'was found', v, 'time(s).')

