# import time
# f = open('hah.txt','rb')
# count = 0
# for i in f:
#     f.seek(200)
#     if count<300:
#         print(i.decode())
#         count = f.tell()
#         print('writed',count)
#     else:
#         print('count',count)
#         break
# print(count)
#
#
#!/usr/bin/python

# Open a file
fo = open("foo.txt", "r")
print ("Name of the file: ", fo.name)


line = fo.readline()
line = fo.readline()
print ("Read Line: %s" % (line))
print(fo.tell())
# Again set the pointer to the beginning
fo.seek(38,0)
line = fo.readline()
print ("Read Line: %s" % (line))

# Close opend file
fo.close()