# Python Program to left rotate the array by d positions
# by rotating one element at a time


#       Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
#       Output: {3, 4, 5, 6, 1, 2}
#       Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

#       Input: arr[] = {1, 2, 3}, d = 4
#       Output: {2, 3, 1}
#       Explanation: The array is rotated as follows:

#       After first left rotation, arr[] = {2, 3, 1}
#       After second left rotation, arr[] = {3, 1, 2}
#       After third left rotation, arr[] = {1, 2, 3}
#       After fourth left rotation, arr[] = {2, 3, 1}












####  Fist Method 


class Rotate_array:

    def rotated_array(self,arr,d):
        d = d % len(arr)
        for i in range(d):
            left = arr[0]
            arr.pop(0)
            arr.append(left)
        return arr
if __name__ == "__main__":
    arr = list(map(int,input("Enter the list element with space: ").split()))
    d = int(input(""Enter value of D to left rotate the array by d positions: "))
    obj = Rotate_array()
    print("Output is: ",obj.rotated_array(arr,d))





## 2second Method


class Rotate_Array:
    def rotateArr(self,arr, d):
        n = len(arr)

        for i in range(d):
        

            first = arr[0]
            for j in range(n - 1):
                arr[j] = arr[j + 1]
            arr[n - 1] = first
        return arr
if __name__ == "__main__":
    arr = list(map(int,input("Enter the list element with space: ").split()))
    d = int(input("Enter value of D to left rotate the array by d positions: "))
    obj = Rotate_Array()
    print("Output is: ",obj.rotateArr(arr,d))

