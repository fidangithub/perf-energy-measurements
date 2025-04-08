def mergeArrays(arr1, arr2):
    def is_ascending(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
    if not is_ascending(arr1):
        arr1.reverse()
    if not is_ascending(arr2):
        arr2.reverse()
    
    i, j = 0, 0
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not merged or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not merged or merged[-1] != arr2[j]:
                merged.append(arr2[j])
            j += 1
        else:
            if not merged or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1
            j += 1
    
    while i < len(arr1):
        if not merged or merged[-1] != arr1[i]:
            merged.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        if not merged or merged[-1] != arr2[j]:
            merged.append(arr2[j])
        j += 1
    
    return merged

  mergeArrays([1,2,3,4], [5,6,7,8])
  mergeArrays([10,8,6,4,2], [9,7,5,3,1])
  mergeArrays([-20,35,36,37,39,40], [-10,-5,0,6,7,8,9,10,25,38,50,62])

  mergeArrays([5,6,7,8,9,10], [20,18,15,14,13,12,11,4,3,2])
  mergeArrays([45,30,20,15,12,5], [9,10,18,25,35,50])
  mergeArrays([-8,-3,-2,4,5,6,7,15,42,90,134], [216,102,74,32,8,2,0,-9,-13])

  mergeArrays([-100,-27,-8,5,23,56,124,325], [-34,-27,6,12,25,56,213,325,601])
  mergeArrays([18,7,2,0,-22,-46,-103,-293], [-300,-293,-46,-31,-5,0,18,19,74,231])
  mergeArrays([105,73,-4,-73,-201], [-201,-73,-4,73,105])
        
  mergeArrays([], [])
  mergeArrays([1,2,3], [])
  mergeArrays([], [5,4,3,2,1])
        