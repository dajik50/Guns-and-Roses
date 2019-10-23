"""
    面向对象购物车
"""


class CommodityModel:
    """
        商品模型
    """

    def __init__(self, id=0, name="", price=0):
        self.id = id
        self.name = name
        self.price = price


class OrderModel:
    """
        订单模型
    """

    def __init__(self, commodity=None, count=0, id=0):
        self.id = id
        self.commodity = commodity
        self.count = count


class ShoppingCartController:
    """
        购物车逻辑控制器
    """
    init_order_id = 0

    def __init__(self):
        self.__list_order = []
        self.__list_commodity_info = self.__load_commodity()

    @property
    def list_order(self):
        return self.__list_order

    @property
    def list_commodity_info(self):
        return self.__list_commodity_info

    def __load_commodity(self):
        """
            加载商品信息
        :return: 商品列表
        """
        return [
            CommodityModel(101, "屠龙刀", 10000),
            CommodityModel(102, "倚天剑", 10000),
            CommodityModel(103, "九阴白骨爪", 8000),
            CommodityModel(104, "九阳神功", 9000),
            CommodityModel(105, "降龙十八掌", 8000),
        ]

    def add_order(self, order_base_info):
        """
            添加订单
        :param order:订单基础信息
        """
        order_base_info.id = self.__generate_order_id()
        self.__list_order.append(order_base_info)

    def __generate_order_id(self):
        """
            生成订单编号
        :return: 订单编号
        """
        ShoppingCartController.init_order_id += 1
        return ShoppingCartController.init_order_id

    def get_total_price(self):
        """
            根据订单计算总价格
        :return:总价格
        """
        total_price = 0
        for item in self.__list_order:
            total_price += item.commodity.price * item.count
        return total_price

    def get_commodity_by_id(self, id):
        """
            获取指定的商品
        :param id: 商品编号
        :return: 商品对象
        """
        for item in self.__list_commodity_info:
            if item.id == id:
                return item


class ShoppingConsoleView:
    """
        购物车控制台界面视图
    """

    def __init__(self):
        self.__controller = ShoppingCartController()

    def __select_menu(self):
        """
            菜单选择　
        """
        while True:
            item = input("1键购买，2键结算。")
            if item == "1":
                self.__buying()
            elif item == "2":
                self.__settlement()

    def __buying(self):
        """
            购买
        """
        self.__print_commodity()
        self.__create_order()
        print("添加到购物车。")

    def __print_commodity(self):
        """
            打印商品信息
        """
        for commodity in self.__controller.list_commodity_info:
            print("编号：%d，名称：%s，单价：%d。" % (commodity.id, commodity.name, commodity.price))

    def __create_order(self):
        """
            创建订单
        """
        while True:
            cid = int(input("请输入商品编号："))
            # 如果该商品存在，则退出循环，否则重新输入。
            commodity = self.__controller.get_commodity_by_id(cid)
            if commodity:
                break
            else:
                print("该商品不存在")
        count = int(input("请输入购买数量："))
        order = OrderModel(commodity, count)
        self.__controller.add_order(order)

    def __settlement(self):
        """
            结算
        """
        self.__print_order()
        total_price = self.__controller.get_total_price()
        self.__pay(total_price)

    def __print_order(self):
        """
            打印订单
        """
        for order in self.__controller.list_order:
            commodity = order.commodity
            print("商品：%s，单价：%d,数量:%d." % (commodity.name, commodity.price, order.count))

    def __pay(self, total_price):
        """
            支付
        :param total_price: 需要支付的价格
        :return:
        """
        while True:
            money = float(input("总价%d元，请输入金额：" % total_price))
            if money >= total_price:
                print("购买成功，找回：%d元。" % (money - total_price))
                self.__controller.list_order.clear()
                break
            else:
                print("金额不足.")

    def main(self):
        """
            界面入口
        """
        while True:
            self.__select_menu()


view = ShoppingConsoleView()
view.main()
