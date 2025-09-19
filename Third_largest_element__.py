##   the task is to find the third largest element an list



class Third_larger:
    @staticmethod
    def thirdLargest(arr):
        n = len(arr)

        first = float('-inf')
        for i in range(n):
            if arr[i] > first:
                first = arr[i]

        second = float('-inf')
        for i in range(n):
            if arr[i] > second and arr[i] < first:
                second = arr[i]

        third = float('-inf')
        for i in range(n):
            if arr[i] > third and arr[i] < second:
                third = arr[i]

        return third

#  input
list1 = list(map(int, input("Enter list elements with space: ").split()))
i = 2  # invalid attempts

while True:
    print("\nMenu:")
    print("1. Find Third Largest")
    print("2. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = Third_larger.thirdLargest(list1)
        print("Third Largest: ", result)

    elif choice == 2:
        print("Exiting...")
        break

    else:
        if i == 0:
            print("Thank you....!")
            break
        print(f"Invalid choice! You can try only {i} more times ")
        i -= 1
