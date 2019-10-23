"""
    2048 游戏核心算法
"""
list_merge = []


# [2,0,2,0]-->[2,2,0,0]
# [2,0,0,2]-->[2,2,0,0]
# [2,4,0,2]-->[2,4,2,0]

# zero_to_end()

# print(list_merge
# 思想：从后往前判断，如果是0则删除，在末尾追加。
def zero_to_end():
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


zero_to_end()
print(list_merge)


# 2.定义函数 marge()
# [2,0,2,0]-->[4,0,0,0]
# [2,0,0,2]-->[4,0,0,0]
# [4,4,4,4]-->[8,8,0,0]
# [2,0,4,2]-->[2,4,2,0]
def merge():
    zero_to_end()
    # 核心思想：零元素后移，判断是否相邻相同。如果是则合并
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)
# 3.向左移动
map=[]
def move_left():
    global list_merge
    for line in map:
        list_merge=line
        merge()
move_left()
print(map)

# 4.向右移动
def move_right():
    global list_merge
    for line in map:
        # 从右往左获取数据形成新列表
        list_merge=(line[::-1])
        # 处理数据
        merge()
        # 将处理后的数据再从右向左还给map
        line[::-1] =list_merge


def square_matrix_transposition(list_matrix):
    for c in range(1, len(list_matrix)):
        for r in range(c, len(list_matrix)):
            # list01[r][c-1] <--> list01[c-1][r]
            list_matrix[r][c - 1], list_matrix[c - 1][r] = list_matrix[c - 1][r], list_matrix[r][c - 1]

# 5.向上移动 move_up 转置  move_lift 转置
def move_up():
    square_matrix_transposition(map)
    move_left()
    square_matrix_transposition(map)

def move_down():
    square_matrix_transposition(map)
    move_right()
    square_matrix_transposition(map)




