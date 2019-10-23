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

