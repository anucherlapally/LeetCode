def mergeOverlappingIntervals(intervals):
    intervals.sort()
    returnList = []
    runningInterval = intervals[0]
    i = 1
    for i in range(1,len(intervals)):
        if runningInterval[1] >= intervals[i][0]:
            runningInterval[1] = max(intervals[i][1], runningInterval[1])
        else:
            returnList.append(runningInterval)
            runningInterval = intervals[i]
    returnList.append(runningInterval)
    return returnList

intervals = [
    [1, 22],
    [-20, 30]
  ]


print(mergeOverlappingIntervals(intervals))
