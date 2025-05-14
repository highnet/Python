def search_for_vowels():
    vowels = set('aeiou')
    word = input("Provide a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print (vowel)
    return found
def search_for_letters(phrase:str, letters:str='aeiou') -> set:
    return set(letters).intersection(set(phrase))
