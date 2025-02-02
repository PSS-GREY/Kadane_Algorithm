
N = int(input("Length of Array: "))

arr = []
for i in range(N):
    arr.append(int(input(f"Enter element {i+1}: ")))

print("Array:", arr)

def kadane(array):
    max_sum = float('-inf')
    curr_sum = 0

    for i in array:
        curr_sum += i
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0

    return max_sum

max_sum = kadane(arr)
print("Maximum sum of subarray:", max_sum)
