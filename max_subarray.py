def maximum_subarray_sum(A, B, C):
    max_sum = 0
    current_sum = 0
    start_index = 0
    
    for end_index in range(A):
        current_sum += C[end_index]
        
        while current_sum > B:
            current_sum -= C[start_index]
            start_index += 1
        
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Get input from the user
A = int(input("Enter the size of array C: "))
B = int(input("Enter the maximum sum allowed (B): "))
C = list(map(int, input("Enter the elements of array C : ").split()))

output = maximum_subarray_sum(A, B, C)
print("Maximum sum of subarray (not exceeding B):", output)