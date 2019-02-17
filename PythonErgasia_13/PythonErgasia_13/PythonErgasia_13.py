def maxDistance(arr, x):
    n = len(list)
    pos_l, pos_r = 0, 0
    l, r, diff = 0, n-1, value 

    while r > l: 
        if arr[l] + arr[r] - x < diff: 
            pos_l = l 
            pos_r = r 
            diff = abs(arr[l] + arr[r] - x) 
      
        if arr[l] + arr[r] > x: 
            r -= 1
        else: 
            l += 1
          
    print("The closest pair is",arr[pos_l],"and",arr[pos_r])
  
value = 10000000   
print("Enter all the numbers of the list:")
list = [int(x) for x in input().split()]
list.sort()
x = int(input("Enter a positive number: "))
maxDistance(list, x) 