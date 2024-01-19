nums = [[1,2,3],[4,5,6],[7,8,9], [10,11,12]]

rows, cols = len(nums), len(nums[0])

for i in range(rows*cols):
    row, col = i // cols, i % cols
    # row, col = divmod(i, cols)
    print(nums[row][col])