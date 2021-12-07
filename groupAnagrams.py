def groupAnagrams(words):

    sortedMap = []

    for i, word in enumerate(words):
        newWord = "".join(sorted(word))
        sortedMap.append({i: newWord})
    
    list1 = sorted(sortedMap, key = lambda x: list(x.values()))
    
    retArray = []
    currentWord = ""
    anagramGroup = []
    for dic1 in list1:
        for key in dic1:
            if dic1[key] == currentWord:
                anagramGroup.append(words[key])
            else:
                if len(anagramGroup) > 0:
                    retArray.append(anagramGroup)
                currentWord = dic1[key]
                anagramGroup = [words[key]]

    if len(anagramGroup) > 0:
        retArray.append(anagramGroup)

    print(retArray)
groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"])