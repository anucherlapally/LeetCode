def findClosestElements(arr, k, x):
    abs_arr = []
    lowest_ind = -1
    lowest_val = float('inf')

    for index, val in enumerate(arr):
        abs_val = abs(x - val)
        abs_arr.append(abs_val)
        if abs_val < lowest_val:
            lowest_val = abs_val
            lowest_ind = index

    left, right = lowest_ind - 1, lowest_ind + 1
    k -= 1

    while k > 0:
        if left < 0:
            right += 1
        elif right >= len(arr):
            left -= 1
        elif abs_arr[left] <= abs_arr[right]:
            left -= 1
        elif abs_arr[left] > abs_arr[right]:
            right += 1

        k -= 1

    
    left += 1

    res = []
    while left < right:
        res.append(arr[left])
        left += 1

    print(res)

    




findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4)




            
        

