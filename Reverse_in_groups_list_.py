###                 ......Reverse an Array in groups of given size......

# Examples:
#       Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], k = 3
#       Output: [3, 2, 1, 6, 5, 4, 8, 7]
#       Explanation: Elements is reversed: [1, 2, 3] → [3, 2, 1], [4, 5, 6] → [6, 5, 4], and the last group [7, 8](size < 3) is reversed as [8, 7]. 
        
#       Input: arr[] = [1, 2, 3, 4, 5], k = 3
#       Output: [3, 2, 1, 5, 4]
#       Explanation: First group consists of elements 1, 2, 3. Second group consists of 4, 5.
        
#       Input: arr[] = [5, 6, 8, 9], k = 5
#       Output: [9, 8, 6, 5]
#       Explanation: Since k is greater than array size, the entire array is reversed.







## Solution


class Reverse_in_groups:
    def reverseingroups(self, arr, k):
        
        length = len(arr) # count the lenght of array 
        
        i = 0 
        while i < length: 
            
            left = i 
            right = i+k-1 
            
            if left < right and right  >=length:
                right = length-1
                
            while left < right :  #  reverse the sub-array [left, right]
                arr[left], arr[right] = arr[right],arr[left]
                left+=1
                right-=1
                
            i +=k
            
        return arr
    

if __name__ == "__main__":
    arr = list(map(int,input("Enter the list element with space: ").split()))
    size = int(input("Enter the groups numbers: "))
    obj = Reverse_in_groups()
    print(obj.reverseingroups(arr,size))
  
