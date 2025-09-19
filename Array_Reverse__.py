

####    Reverse an array arr[]






## 1.... using swap mehtod
class Reverselist:

    def reverse_list(self,arr):
        le = len(arr)
        left = 0
        right = le-1
        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left+=1
            right-=1

        return arr
list1 = list(map(int,input("Enter the element(num) with space: ").split()))
obj = Reverselist()
print(obj.reverse_list(list1))








###   2nd.....using the temporary list to store elements

class Reverse_list:

    def rev_list(self,arr):
        n = len(arr)

        # Temporary list to store elements
        # in reversed order
        temp = [0] * n
    
        # Copy elements from original array
        # to temp in reverse order
        for i in range(n):
            temp[i] = arr[n - i - 1]
    
        # Copy elements back to original array
        for i in range(n):
            arr[i] = temp[i]
        return arr
if __name__ == "__main__":
    arr = list(map(int,input("Enter the list element with space: ").split()))
    obj = Reverse_list()
    print(obj.rev_list(arr))
