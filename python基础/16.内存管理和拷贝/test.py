"""---author==hxj---"""
# import pygame,sys
#
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode([640,480])
# pygame.time.delay(1000)
# pygame.mixer.music.load('files/许巍 - 蓝莲花.mp3')  # 加载音乐
# pygame.mixer.music.play()
#
# import pygame,sys
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode([640,480])
# pygame.time.delay(1000)
# pygame.mixer.music.load('files/许巍 - 蓝莲花.mp3')
# pygame.mixer.music.play()
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()


# import time


# class Song:
#     def __init__(self, minute, second, millisecond):
#         self.minute = minute
#         self.second = second
#         self.millisecond = millisecond
#         self.time1 = None
#         self.lyric = None
#
#     @staticmethod
#     def read_lyric():  #这个对象方法负责读文本内容按行读
#         with open('files/lanlianhua.txt', 'r', encoding='utf-8') as f:
#             return f.readlines()
#
#     def print_lyric(self):
#         while self.minute < 3:
#             self.millisecond += 1
#             if self.millisecond == 60:
#                 self.second += 1
#                 self.millisecond = 0
#             elif self.second == 60:
#                 self.minute += 1
#                 self.second = 0
#             self.time1 = '['+str(self.minute).rjust(2, '0')+':'+str(self.second).rjust(2, '0')\
#                          + '.'+str(self.millisecond).rjust(2, '0')+']'
#             print(self.time1)    #每微妙开始读
#             for self.lyric in Song.read_lyric():
#                 if self.time1 in self.lyric[:self.lyric.rfind(']')+1]:    #读到与文本相同时间歌词就打印
#                     print(self.lyric[self.lyric.rfind(']')+1:])
#                     time.sleep(0.8)
#                     break
#
#
# p1 = Song(0, 0, 0)
# p1.print_lyric()
# class Lyric:
#     def __init__(self, time, word):
#         value = float(time[1:3])*60 + float(time[4:])
#         self.time = value
#         self.word = word
#
#     def __repr__(self):
#         return str(self.time) + ':' + self.word
#
#     def __gt__(self, other):
#         return self.time > other.time
#
#
# class LyricAnalysis:
#
#     def __init__(self, name):
#         # 歌名
#         self.name = name
#         self.__all_lyrics = []
#
#     def get_word(self, time):
#         # =======解析歌词文件======
#         if not self.__all_lyrics:
#             print('解析歌词')
#             with open('files/'+self.name, encoding='utf-8') as f:
#                 while True:
#                     line = f.readline()
#                     if not line:
#                         break
#                     lines = line.split(']')
#                     word = lines[-1]
#                     for t in lines[:-1]:
#                         lyric = Lyric(t, word)
#                         self.__all_lyrics.append(lyric)
#             print(self.__all_lyrics)
#             # 排序
#             self.__all_lyrics.sort(reverse=True)
#
#         # ==========获取歌词==========
#         for lyric in self.__all_lyrics:
#             if lyric.time <= time:
#                 return lyric.word
#
#
# ly = LyricAnalysis('jian.txt')
# print('===:', ly.get_word(123))
# print('===:', ly.get_word(10))
# print('===:', ly.get_word(89))
# class LyricAnalysis:
#     def __init__(self, name):
#         self.name = name
#         self.all_lyric = []
#
#     def get_lyric(self):
#         with open('files/'+self.name, encoding="utf-8")as f:
#             f.readline()
#             for x in f:
#                 # print("=")
#                 line = x.split("]")
#                 self.all_lyric.append(line)
#         print(self.all_lyric)
#
#
# c1 = LyricAnalysis('jian.txt')
# c1.get_lyric()
tuple3 = 1, 2, 3
print(tuple3)

tuple1 = ('abc')
tuple2 = ('abc',)
print(tuple1)
print(tuple2)
print(type(tuple1))
print(type(tuple2))
a = 1,
print(a)