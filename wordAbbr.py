def valid_word_abbreviation(word, abbr):

    pword, pabbr = 0, 0
    
    while pabbr < len(abbr):
        if abbr[pabbr].isdigit():
            if abbr[pabbr] == '0':
                return False
            
            counter = ""
            p = pabbr
            while p < len(abbr) and abbr[p].isdigit():
                counter += abbr[p]
                p += 1
            counter = int(counter)

            pword += counter
            
            pabbr = p
        else:
            if pword >= len(word) or pabbr >= len(abbr):
                return False
            if word[pword] != abbr[pabbr]:
                return False
        
            pabbr += 1
            pword += 1
    
    if pword != len(word):
        return False
    return True


print(valid_word_abbreviation('rxbehdcmpygfsurufnbf', 'r2e333u2f'))