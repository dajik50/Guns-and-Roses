class StudentModel:
    """
        学生数据模型
    """

    def __init__(self, name="", age=0, score=0.0):
        self.id = 0  # 真实数据在添加学生时确定
        self.name = name
        self.age = age
        self.score = score

