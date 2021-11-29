def longestPalindromicSubstring(string):
	currentLongest = [0,1]
	for i in range(len(string)):
		odd = getPalindromeLength(string, i - 1, i + 1)
		even = getPalindromeLength(string, i - 1, i)
		longest = max(odd, even, key=lambda x: x[1] - x[0])
		currentLongest = max(currentLongest, longest, key=lambda x: x[1] - x[0])
	
	return string[currentLongest[0]: currentLongest[1]]
		

def getPalindromeLength(string, left, right):
	while left >= 0 and right < len(string):
		if string[left] != string[right]:
			break
		left -= 1
		right += 1
	return [left + 1, right]

		
				
			
print(longestPalindromicSubstring("abaxyzzyxf"))