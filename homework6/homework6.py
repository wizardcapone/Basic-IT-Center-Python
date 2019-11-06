arr = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end="\t")
    print("", end="\n")
    print()
for i in range(0, len(arr)):
    for j in range(len(arr)-i-1, len(arr)):
        print(arr[i][j], end="\t")
    print()
