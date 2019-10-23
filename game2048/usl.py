"""
    游戏界面控制器，负责处理游戏界面逻辑．
"""
import os

from bll import GameCoreController


class GameConsoleView:
    def __init__(self):
        self.__concoller = GameCoreController()

    def __start(self):
        # 产生一个随机数
        self.__concoller.generate_number()
        # 产生一个随机数
        self.__concoller.generate_number()
        # 绘制界面
        self.__draw_map()


    def __draw_map(self):
        # os.system(系统命令)
        os.system("clear")
        for line in self.__concoller.map:
            for item in line:
                print(item,end= "\t")
            print()
        print("当前分数%d"%self.__concoller.n)

    def __update(self):
        while True:
            # 根据输入移动地图
            self.__move_map_for_input()
            # 产生一个数字
            self.__concoller.generate_number()
            # 绘制界面
            self.__draw_map()
            # 判断游戏是否结束
            if self.__concoller.is_game_over():
                print("游戏结束")
                break

    def __move_map_for_input(self):
        dir = input("请输入：")
        if dir == "w":
            self.__concoller.move_up()
        elif dir == "s":
            self.__concoller.move_down()
        elif dir == "a":
            self.__concoller.move_left()
        elif dir == "d":
            self.__concoller.move_right()

    def main(self):
        self.__start()
        self.__update()