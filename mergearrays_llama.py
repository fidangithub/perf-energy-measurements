def mergeArrays(arr1, arr2):
  
    combined = arr1 + arr2
    
    unique = set(combined)
    
    sorted_unique = sorted(list(unique))
    
    return sorted_unique


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
        