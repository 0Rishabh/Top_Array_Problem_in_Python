



#       Given an array of integers arr[] of
#       size N, find the two smallest integers
#       in the array and form the 
#       largest possible number using them.
#       Output this largest number
        
        
#      arr =  [1, 2, 3, 4, 5, 6, 7]
#       Testcase Output
#       21
#       Explanation
#       The two minimum numbers out of the
#       given array are 1 and 2. If we try to make 
#       the largest number possible using these two
#       numbers, we get 21.





def find_largest_number(arr):
    smallest = sorted(arr)[:2]
    a, b = smallest[0], smallest[1]
    
 
    num1 = int(str(a) + str(b))
    num2 = int(str(b) + str(a))
    

    return max(num1, num2)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_largest_number(arr)
    print(result)
