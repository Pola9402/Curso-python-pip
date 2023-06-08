def pick_peaks(arr):
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i+1]:
            # print(arr[i])
            break
    for i in range(arr[i],len(arr)-1):
        print(arr[i])
        if arr[i] > arr[i+1]:
            # print(arr[i])
            break



arr = [1,2,3,6,4,1,2,3,2,1]
pick_peaks(arr)