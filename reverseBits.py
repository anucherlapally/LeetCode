def reverseBits(n: int) -> int:
        
    result = 0 #initialize the result to zero
    
    for i in range(32):
        result = result << 1 #left shift the bits in result (last digit from the original number will be the left most here)
        if n & 1 == 1: #check if last digit in original num is 1
            result += 1 #if yes add 1 to result
        n = n >> 1 #right shift original num, as the last number here is taken care of
    
    return result

print(reverseBits(43261596))