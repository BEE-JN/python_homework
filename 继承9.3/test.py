# coding=utf-8
# author:GCS


# 编写一个名为IceCreamStand的类，让它继承你之前完成的Restaurant类，添加一个flavors的属性，
# 用于储存一个由各种口味冰激凌组成的列表，编写一个显示这些冰激凌的方法
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is runing!")

    def set_number_served(self, number):
        self.number_served = number
        print("There have been " + str(self.number_served) + "students ate in " + self.restaurant_name)

    def increment_number_served(self, number):
        self.number_served += number
        print("There have been " + str(self.number_served) + "students ate in " + self.restaurant_name)


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served=0)
        self.flavors = ["草莓", "黑莓", "菠萝", "香蕉"]

    def read_icecream(self):
        print("The stand has: ", end="")
        for flavor in self.flavors:
            print(flavor + " ", end="")


IceCreamStand1 = IceCreamStand("冰激凌店", "冰激凌")
IceCreamStand1.describe_restaurant()
IceCreamStand1.open_restaurant()
IceCreamStand1.set_number_served(100)
IceCreamStand1.increment_number_served(50)
IceCreamStand1.read_icecream()


# 在User类中添加一个名为privileges的属性，用于储存一个字符串组成的列表
# 编写一个show_privileges()的方法，它显示管理员员的权限，创建一个admin实例
class User():
    def __init__(self, first_name, last_name, age, sex, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = login_attempts

    def describe_user(self):
        print("\nName: " + self.first_name + self.last_name +
              "\nAge: " + str(self.age) + "\nSex: " + self.sex)

    def greet_user(self):
        print("Hello! " + self.first_name + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("登录次数： " + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("登录次数： " + str(self.login_attempts))


class Admin(User):
    def __init__(self, first_name, last_name, age, sex, login_attempts=0):
        super().__init__(first_name, last_name, age, sex, login_attempts=0)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("You ", end="")
        for privilege in self.privileges:
            print(privilege + ",", end="")


new_admin = Admin("郭", "崇山", 19, "boy")
new_admin.describe_user()
new_admin.greet_user()
new_admin.show_privileges()
print("\n")


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + "miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximagtely " + str(range)
        message += "miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            print("汽车已经升级电瓶")
            self.battery_size = 85

my_car = ElectricCar("五菱宏光", "魔改5人小面包", 2018)
car_name = my_car.get_descriptive_name()
print(car_name)
my_car.read_odometer()
my_car.update_odometer(50)
my_car.increment_odometer(10)
my_car.read_odometer()
my_car.battery.describe_battery()
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()
