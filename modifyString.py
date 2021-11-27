def modifyString(s: str) -> str:
    ret = ""
    if len(s) == 1 and s == "?":
        return 'a'
    elif len(s) == 1:
        return s
    
    for i in range(len(s)):
        
        if s[i] == '?':
            ordChar = ord('a')
            if i == 0:
                while ord(s[i + 1]) == ordChar:
                    ordChar += 1
            elif i == len(s) - 1:
                while(ord(ret[i - 1]) == ordChar):
                    ordChar += 1
            else:
                while(ord(ret[i-1]) == ordChar or ord(s[i +1]) == ordChar):
                    ordChar += 1
            
            ret += chr(ordChar)
        else:
            ret += s[i]
        
    return ret
            