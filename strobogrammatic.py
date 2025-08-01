def is_strobogrammatic(num):
  
    left, right = 0, len(num) - 1
    
    while left < right:
        if num[left] in [2,4,5,7]:
            return False
        
        if num[left] == num[right]:
            left += 1
            right -= 1
        elif num[left] == '6' and num[right] == '9':
            left += 1
            right -= 1
        elif num[left] == '9' and num[right] == '6':
            left += 1
            right -= 1
        
        else:
            return False
            
    return True
is_strobogrammatic("619")