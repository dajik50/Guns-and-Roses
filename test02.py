list01 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

for i in range(1, len(list01)):
    for t in range(i, len(list01)):
        list01[i-1][t], list01[t][i-1] = list01[t][i-1], list01[i-1][t]
print(list01)



