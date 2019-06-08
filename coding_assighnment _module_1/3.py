 
def binarySearch (arr, f, r, x):
    if r >= f: 
  
        mid = f + (r - f)//2
  
        if arr[mid] == x: 
            return mid 
          
        elif arr[mid] > x: 
            return binarySearch(arr, f, mid-1, x)
        else: 
            return binarySearch(arr, mid + 1, r, x)
    else: 
      
        return -1
  
arr=input("enter the array elemets: ").split(" ")
x=input("enter the number u want to search for: ")
  
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("the given number is at position" ,result)
else: 
    print ("the given number isnt present")
