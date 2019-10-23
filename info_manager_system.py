"""
    信息管理系统
        信息 -- 学生信息

    步骤：
        （一）
        数据模型类：StudentModel
            数据：编号 id,姓名 name,年龄 age,成绩 score
        逻辑控制类：StudentManagerController
            数据：学生列表 __stu_list
            行为：获取列只读属性 stu_list,
                 添加学生 add_student(stu_info)
                      给stu_info创建学生编号
                      存储学生
        测试：添加学生功能、获取所有学生功能.
        （二）在逻辑控制类中，完成删除学生功能，返回是否删除成功.
              remove_student(stu_id)
        （三）修改学生
             update_studenet(stu_info)
                在学生列表中，根据stu_info.id查找学生对象
                修改其信息
        （四）根据成绩从大到小排序order_by_score()
        （五）创建界面视图类StudentManagerView
               显示菜单__display_menu()
                     print("1....")
               选择菜单 __select_menu():
                     if input("请输入：") == "1":
                          __input_students():
               入口 main():
                    while True:
                      __display_menu()
                      __select_menu()

               录入学生信息 __input_students():
                    while True:
                          input("请输入姓名:")...
                          调用控制器中的add_student方法
        （六）显示所有学生信息
         (七) 删除学生__delete_student
                 获取需要删除的学生编号
                 调用控制器中的remove_student方法
                 提示："删除成功"  或者 "删除失败"
         (八)修改学生信息__modify_student()
                获取需要修改的学生信息
                调用控制器中的update_student方法
         (九) 按照成绩从高到低显示
                16:50
"""


class StudentModel:
    """
        学生数据模型
    """

    def __init__(self, name="", age=0, score=0.0):
        self.id = 0  # 真实数据在添加学生时确定
        self.name = name
        self.age = age
        self.score = score


class StudentManagerController:
    """
        学生管理控制器：主要负责处理程序的主要逻辑（算法）。
    """
    # 学生的初始编号
    __init_id = 1000

    @classmethod
    def __generate_id(cls):
        cls.__init_id += 1
        return cls.__init_id

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu_info):
        """
            添加学生，由界面获取学生信息方法调用。
        :param stu_info:需要添加的学生对象(信息)
        """
        stu_info.id = StudentManagerController.__generate_id()
        self.__stu_list.append(stu_info)

    def remove_student(self, stu_id):
        for item in self.__stu_list:
            if item.id == stu_id:
                self.__stu_list.remove(item)
                return True  # 删除成功
        return False  # 删除失败

    def update_student(self, stu_info):
        """
            根据stu_info.id修改学生的信息(stu_info.name/stu_info.age..)
        :param stu_info:需要修改的学生信息
        :return:是否修改成功
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.score = stu_info.score
                item.age = stu_info.age
                return True  # 修改成功
        return False  # 修改失败

    def order_by_score(self):
        for r in range(len(self.__stu_list)):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score < self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], self.__stu_list[r]


class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("""
1) 添加学生信息
2) 显示学生信息
3) 删除学生信息
4) 修改学生信息
5) 按照成绩从高到低显示 
        """)

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__outout_student_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_students(self):
        while True:
            name = input("请输入姓名:")
            age = int(input("请输入年龄:"))
            score = float(input("请输入成绩:"))
            stu = StudentModel(name, age, score)
            # StudentManagerController().add_student(....)
            self.__manager.add_student(stu)
            if input("输入e退出:") == "e":
                break

    def __output_students(self):
        for item in self.__manager.stu_list:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        id = int(input("请输入需要删除的编号："))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.id = input("请输入需要修改的学生编号：")
        stu.name = input("请输入需要修改的学生姓名：")
        stu.age = input("请输入需要修改的学生年龄：")
        stu.score = input("请输入需要修改的学生成绩：")

        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __outout_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students()


# 测试.....................
view = StudentManagerView()
view.main()

"""
manager = StudentManagerController()
s01 = StudentModel("赵敏", 26, 100)
manager.add_student(StudentModel("灭绝", 56, 85))
manager.add_student(s01)

# manager.remove_student(1002)
s02 = StudentModel("敏儿", 27, 95)
s02.id = 1001

manager.update_student(s02)

# 内部修改实例变量__stu_list
manager.order_by_score()

# 获取属性(实例变量__stu_list)
for item in manager.stu_list:
    print(item.name, item.score)
"""