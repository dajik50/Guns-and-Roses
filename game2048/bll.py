"""
    游戏逻辑控制器，负责处理游戏核心算法．
"""
import random


class GameCoreController:
    def __init__(self):
        # 合并数据时使用的列表
        self.__list_merge = None
        # 生成新数字时使用的列表
        self.__list_empty_location = []

        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.n = 0

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移动到末尾.
        """
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合并
        """
        self.__zero_to_end()

        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                if self.__list_merge[i + 1] != 0:
                    self.n += 1
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        """
            向左移动
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        """
            向右移动
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def move_up(self):
        self.__square_matrix_transpose()
        self.move_left()
        self.__square_matrix_transpose()

    def move_down(self):
        self.__square_matrix_transpose()
        self.move_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        """
            方阵转置
        :param sqr_matrix: 二维列表类型的方阵
        """
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]

    def generate_number(self):
        """
            生成新数字
        """
        self.__get_empty_location()
        # 随机选择一个
        tuple_location = random.choice(self.__list_empty_location)
        number = self.__select_random_number()
        self.__map[tuple_location[0]][tuple_location[1]] = number
        # 如果使用了该位置，就应该从列表中删除
        self.__list_empty_location.remove(tuple_location)

    def __select_random_number(self):
        """
            选择随机数字
        """
        return 4 if random.randint(1, 10) == 1 else 2

    def __get_empty_location(self):
        """
            找出所有空白位置
        :return:
        """
        # 计算前，先清空之前统计过的数据.
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[0])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append((r, c))

    def is_game_over(self):
        """
            游戏是否结束
        """
        for i in range(len(self.__map)):
            for item in range(len(self.__map[i])):
                if self.__map[i][item] == 2048:
                    return True
        if len(self.__list_empty_location) > 0:
            return False

        # 横向判断
        # # 00  01   02   03
        # for r in range(len(self.__map)):
        #     for c in range(len(self.__map[0]) - 1):
        #         if self.__map[r][c] == self.__map[r][c + 1]:
        #             return False
        # 竖向判断
        # # 00  10   20   30
        # for c in range(len(self.__map[0])):
        #     for r in range(len(self.__map) - 1):
        #         if self.__map[r][c] == self.__map[r + 1][c]:
        #             return False

        # 横竖判断
        for r in range(len(self.__map)):  # 0
            for c in range(len(self.__map[0]) - 1):  # 012
                if self.__map[r][c] == self.__map[r][c + 1] or self.__map[c][r] == self.__map[c + 1][r]:
                    return False
        return True

    # ---------测试代码--------------


if __name__ == "__main__":
    controller = GameCoreController()
    # controller.move_left()
    # print(controller.map)
    # controller.move_down()

