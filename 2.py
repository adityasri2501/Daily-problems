size = int(input("Enter the size of the array = "))
arr = []
for i in range(size):
    arr.append(int(input("Enter the value = ")))
final_arr = sorted(set(arr))
length = len(final_arr)
if (length < 2):
    print("The runner-up score does not exist.")
else:
    print(f"Runner-up score = {final_arr[length-2]}")