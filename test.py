# from model import *
import csv

text = '''Date,User,Message
2016-08-07 00:12:07,"임준오","h"
2016-08-07 00:28:16,"OI우형","hi"
2016-08-07 00:30:20,"홍인표","김연경이 누구임"
2016-08-07 00:30:42,"홍인표","연애인임?"
2016-08-07 00:31:27,"윤철민","ㄴㄴ"
2016-08-07 00:31:29,"정재원","배구국대"
2016-08-07 00:31:45,"정재원","사진"
2016-08-07 00:31:58,"정재원","난 펜싱 볼거다 이기야"
2016-08-07 00:32:09,"윤철민","ㅎ.ㅎ"
2016-08-07 00:32:25,"정재원","아람찡..."
2016-08-07 00:35:01,"윤철민","앙?"
2016-08-07 00:35:20,"OI우형","터키에서"
2016-08-07 00:35:21,"OI우형","뛰는"
2016-08-07 00:35:22,"OI우형","공격수"
2016-08-07 00:37:17,"정재원","?"
2016-08-07 00:37:27,"정재원","ㅁㅊ신아람 32강 탈락했었냐"'''

text = text.split('\n')[1:]
for i in range(len(text)):
    text[i] = text[i].split(',')[1].replace('"','')
# return len(set(text))

# # print(text)
# text.reverse()
# for t in text[0:2]:
#     print(t.split(',')[2].replace('"', ''))
# print(text[0:2])
#
