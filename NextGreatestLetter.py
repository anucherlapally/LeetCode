from typing import List

def nextGreatestLetter(letters: List[str], target: str) -> str:
        
        start = 0
        end = len(letters) - 1
        
        while start <= end:
            
            mid = (start + end) // 2
            
            if(letters[mid] > target and letters[mid - 1] <= target):
                return letters[mid]
            elif(letters[mid] > target):
                end = mid - 1
            elif(letters[mid] <= target):
                start = mid + 1
            elif mid == end:
                return letters[0]
            
        if(letters[mid] > target):
            return letters[mid]
        if mid == end:
            return letters[0]
        
print(nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"],"e"))