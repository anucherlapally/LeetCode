def reverseWordsInString(string):

    print(helper(string, 0))

def helper(string, i):
    if i == len(string):
        return ''
    else:
        word = ""
        space = ""
        while i < len(string) and string[i] != ' ':
            word += string[i]
            i += 1
        while i < len(string) and string[i] == ' ':
            space += string[i]
            i += 1
        return helper(string, i) + space + word


print(reverseWordsInString("hat em!     lit lot off"))