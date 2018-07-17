# coding=utf-8
# author:GCS

# 创建多个字典，对于每个字典都使用一个宠物的名称来给 他命名，在每个字典中，包含宠物的类型和它主人的名字。
# 将这些字典储存在一个名为pets的列表中，再遍历该列表，并将宠物的所有信息都打印出来

pet1 = {
    'type': 'dog',
    'owner': 'boy',
}
pet2 = {
    'type': 'cat',
    'owner': 'next',
}
pet3 = {
    'type': 'bird',
    'owner': 'the',
}
pets = [pet1,pet2,pet3]
for pet in pets:
    print(pet)
    print(pet.keys())
    print(pet.values())

# 创建一个叫favorite_places的字典，将3个人名用作键，对于每个人，都储存它最喜欢的1-3个地方
favorite_places = {
    'a': ["株洲","长沙","湘潭"],
    'b': ["美国","日本","韩国"],
    'c': ["天堂"],
}
for name,places in favorite_places.items():
    if len(places)>1:
        print(name + " favorite place are ")
    else:
        print(name + " favorite place is ")
    for place in places:
        print(place)

# 创建一个名为cities的字典，将3个城市用作键，对于每个城市名都创建一个字典，并在其中
# 包含城市所在的国家，人数 包含country population键
cities = {
    '株洲': {
        'country': '中国',
        'population': '100000',
    },
    '纽约': {
        'country': '美国',
        'population': '2000000',
    },
    '巴黎': {
        'country': '法国',
        'population': '2000000',
    }
}
for city,city_info in cities.items():
    print("\nCity:" + city)
    country = city_info['country']
    population = city_info['population']
    print("Country: " + country)
    print("Population: " + population)