def kthCharacter(k: int) -> str:

        word = 'a'

        k_char = genNewWord(k, word)

        return k_char

def genNewWord(k, word):
    if len(word) > k:
        return word[k - 1]

    new_word = word

    for char in word:
        if char == 'z':
            new_word += 'a'
        else:
            new_word += chr(ord(char) + 1)

    
    return genNewWord(k, new_word)

        
print(kthCharacter(15))