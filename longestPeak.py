def longestPeak(array):
    count = 1
    maxCount = 0
    incr = False
    decr = False
    isPeak = False
    for i in range(1,len(array)):

        if array[i] > array[i-1]:
            if decr and isPeak:
                if maxCount < count:
                    maxCount = count
                    count = 1
                decr = False
                isPeak = False
            count += 1
            incr = True
        
        elif array[i] < array[i-1]:
            if incr:
                isPeak = True
                count += 1
            decr = True
        else:
            if decr and isPeak:
                if maxCount < count:
                    maxCount = count
                decr = False
                isPeak = False
            count = 1
            incr = False
            decr = False
	
    if incr and decr and isPeak:
        if maxCount < count:
            maxCount = count
    return maxCount


			

			
longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])