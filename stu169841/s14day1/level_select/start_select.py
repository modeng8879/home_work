# -*- coding: UTF-8 -*-
message_dict = {
    "sichuan":{"guanggan":["wusheng",'yuechi',"linshui"],"guangyan":["wangcang","changxi","guangyuanshiqu"]},
    "beijing":{"haidian":["zhongguancun","wudaokou","shangdi"],"changyang":["changying","guomao","guangzhuang"]}
}

def select(city_name,city_dict):
    return city_dict[city_name]

one = message_dict.keys() #["sichuan","beijing" ]
#print city list
for i in one:
    print one.index(i), i

city_num = raw_input("请输入城市对应的数字：")
#print two level city list
if city_num.isdigit():
    two = select(one[int(city_num)],message_dict)
    for i in two.keys():
        print two.keys().index(i),i

city2_num = raw_input("请输入城市对应的数字：")

if city2_num.isdigit():
    city =  select(two.keys()[int(city2_num)],two)
    for i in city:
        print city.index(i),i
