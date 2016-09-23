# import time
# current_time = time.localtime(time.time())
# print(time.time())
# print(current_time)
# time_form = "%a %b %d %H:%M:%S %Y"
#
# # str_time = time.strftime(time_form,current_time)
# str_time = time.asctime()
# print(str_time)
#
#
# print(time.mktime(time.strptime(str_time,time_form)))

# import datetime
# import time
# print(datetime.datetime.now())
# print(datetime.date.fromtimestamp(time.time()))
#
# print(datetime.datetime.now())
# print(datetime.datetime.now() + datetime.timedelta(3))
# print(datetime.datetime.now() + datetime.timedelta(-3))




# import random
# def auth_code(x):
#     checkcode = ''
#     for i in range(x):
#         current = random.randrange(0,x)
#         if current != i:
#             temp = chr(random.randint(65,90))
#
#         else:
#             temp = random.randint(0,9)
#         checkcode += str(temp)
#     return checkcode
#
# print(auth_code(6))

# import configparser
# confi_parser =  configparser.ConfigParser()
# print(confi_parser)
# confi_parser["DEFAULT"] = {
#     "ServerAliveInterval" : '45',
#     "Compression" : "yes",
#     "ConmpressinLevel" : '9',
#     "ForwardX11" : 'no'
#                            }
# confi_parser["bitbucket.org"] = {}
# bitbucket = confi_parser['bitbucket.org']
#
# bitbucket['User'] = 'hg' # {bitbucket.org:{"User" : "hg"}}
#
#
# confi_parser['topsecret.server.com'] = {}
# topsecret = confi_parser['topsecret.server.com']
#
# topsecret["Host Port"] = "50022"
# topsecret["ForwardX11"] = 'no'
# confi_parser['DEFAULT']['ForwardX11'] = 'yes'
#
#
# with open('example.ini', 'w') as configfile:
#    confi_parser.write(configfile)

# import configparser
# parserresult = configparser.ConfigParser()
# parserresult.read('example.ini')
# a= parserresult.sections()
# print(a)
# print(parserresult.options("bitbucket.org"))
# sec = parserresult.has_section('group2')
# print(sec)
# sec = parserresult.add_section('group2')
# parserresult.set()
#
# parserresult.write(open('i.cfg', "w"))
#
# print(parserresult.items("bitbucket.org"))
#
# parserresult.set('group2','k1',11111)
# parserresult.write(open('i.cfg', "w"))