
# the task is to find second largest distinct element in the array.


class Second_Lar:
    @staticmethod
    def find_sec_lar(arr):
        larger = -1
        sec_lar = -1

        for i in arr:
            if i > larger:
                sec_lar = larger
                larger = i
            elif i < larger and i > sec_lar:
                sec_lar = i

        return sec_lar


list1 = list(map(int, input("Enter list elements with space: ").split()))
i = 2

while True:
    print("\tMenu:")
    print("\t1. Find Second Largest")
    print("\t2. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = Second_Lar.find_sec_lar(list1)
        print("Second Largest: ", result)
    elif choice == 2:
        print("Exiting...")
        break
    else:
        if i == 0:
            print("Thank you....!")
            break
        
        print(f"Invalid choice! You can try only {i} times ")
        

        i-=1
