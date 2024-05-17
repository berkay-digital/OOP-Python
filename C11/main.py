import numpy as np

A = np.random.randint(0, 10, (4, 4))
B = np.eye(4)

sum_AB = np.add(A, B)
print("Sum of A and B:\n", sum_AB)

total_sum = np.sum(A) + np.sum(B)
print("Sum of all numbers in both arrays A and B:", total_sum)

max_A = np.max(A)
print("Maximum value in A:", max_A)

A_reshaped = A.reshape((8, 2))
B_reshaped = B.reshape((2, 8))
product_AB = np.matmul(A_reshaped, B_reshaped)
print("Product of reshaped A and B:\n", product_AB)

sum_third_col_A = np.sum(A[:, 2])
sum_third_row_B = np.sum(B[2, :])
total_sum_third = sum_third_col_A + sum_third_row_B
print("Sum of values from the third column in A and third row in B:", total_sum_third)

A[:, 1] = np.square(A[:, 1])
print("A after squaring values in second column:\n", A)

AB_joined = np.hstack((A, B))
print("A and B joined horizontally:\n", AB_joined)

A_str = A.astype(str)
B_str = B.astype(str)
AB_str = np.char.add(A_str, B_str)
print("A and B as strings added:\n", AB_str)


matrix = np.full((2, 3), 2)
matrix2 = np.array([[3, 4, 5], [6, 7, 8], [9, 10, 11]])
matrix2_T = matrix2.T
result = np.matmul(matrix, matrix2_T)

print(matrix)
print(matrix2_T)
print(result)


ex_matrix = np.array([[3, 4, 5], [6, 7, 8], [9, 10, 11]])
ex_matrix_T = ex_matrix.T
ex_matrix2 = np.full((2, 3), 2)
# result2 = np.matmul(ex_matrix_T, ex_matrix2)
# print(result2)
# Error
