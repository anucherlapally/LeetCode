def taskAssignment(k, tasks):

    indices = [i for i in range(len(tasks))]

    indices.sort(key = lambda x: tasks[x])

    taskArray = []
    for i in range(k):
        length = len(tasks) - 1
        taskArray.append([indices[i], indices[length - i]])
    
    return taskArray

print(taskAssignment(7, [2, 1, 3, 4, 5, 13, 12, 9, 11, 10, 6, 7, 14, 8]))