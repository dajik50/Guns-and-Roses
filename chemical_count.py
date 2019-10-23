m = 0
# m为计数变量
chemical_element = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "l", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
# 这是总的列表可以一直往里加

for element01 in chemical_element[0:len(chemical_element):]:
    # 从第一个开始取到列表最后一个
    for element02 in chemical_element[len(chemical_element):-1:-1]:
        # 从最后一个取到第一个
        if element01 == 0:
            del element01
        elif element02 == 0:
            del element02
            # 这俩随便写的判定条件
        elif element01 == element02:
            break

        # 如果结果一样 结束循环
        m += 1
        # 循环次数 也就是多少个计算方法
        element01 += element02
        # 这里放你想计算的代码 我写的01等于01+02
