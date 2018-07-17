# coding=utf-8
# author:GCS

# 创建一个名为Restaurant的类，其方法_inti_()设置两个变量，创建两个方法，第一个打印消息
# 第二个表示餐厅正在营业


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type,number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is runing!")

    def set_number_served(self,number):
        self.number_served = number
        print("There have been " + str(self.number_served) + "students ate in "  + self.restaurant_name)

    def increment_number_served(self,number):
        self.number_served += number
        print("There have been " + str(self.number_served) + "students ate in " + self.restaurant_name)

the_restaurant = Restaurant("江南大学一食堂","甜的一逼的菜")
print(the_restaurant.restaurant_name + " " +the_restaurant.cuisine_type)
the_restaurant.describe_restaurant()
the_restaurant.open_restaurant()

another_restaurant = Restaurant("江南大学三食堂","口味不错的菜")
another_restaurant.describe_restaurant()
another_restaurant.open_restaurant()
another_restaurant.set_number_served(50000)
another_restaurant.increment_number_served(1000)

# 创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会储存的其他几个属性
# 在类User中定义一个方法，打印用户信息摘要，在定义一个方法想用户发出问候
class User():
    def __init__(self,first_name,last_name,age,sex,login_attempts=0):
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

new_user = User("郭","崇山","19","男")
new_user.describe_user()
new_user.greet_user()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.reset_login_attempts()
new_user.increment_login_attempts()