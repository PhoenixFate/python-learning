import string


class HouseItem:

    def __init__(self, name: string, area: float):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type: string, area: float):
        # 户型
        self.house_type = house_type
        # 房子面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.item_list = []

    def add_item(self, item: HouseItem):
        # 1.判断家具面积，太大，不能添加
        if item.area > 5 or item.area > self.free_area:
            print("家具面积太大，放不下")
            return
        # 2.将家具的名称添加到列表
        self.item_list.append(item.name)

        # 3.计算剩余面积
        self.free_area -= item.area
        print("要添加的家具:%s " % item)

    def __str__(self):
        # python能够自动的将一对（）里面的内容连接在一起
        return ("户型:%s\n总面积:%.2f\n剩余面积: %.2f\n家具: %s"
                % (self.house_type, self.area, self.free_area, self.item_list))


# 1.创建家具
bed = HouseItem("席梦思", 4.23)
wardrobe = HouseItem("衣柜", 2.1)
table = HouseItem("餐桌", 1.23)

print(bed)
print(wardrobe)
print(table)

# 2.创建House
house = House("公寓", 120.4)

# 3.添加家具
house.add_item(bed)
house.add_item(wardrobe)
house.add_item(table)
print(house)
