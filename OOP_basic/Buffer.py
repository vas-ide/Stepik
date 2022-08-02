

class Buffer:

    def __init__(self):
        self.buffer_lst = []

    def add(self, *a):
        for i in a:
            self.buffer_lst.append(i)
            if len(self.buffer_lst) == 5:
                sum_lst = 0                     # print(sum(self.buffer_lst))
                for j in self.buffer_lst:       # self.buffer_lst.clear()
                    sum_lst += j
                print(sum_lst)
                self.buffer_lst = []

    def get_current_part(self):
        return self.buffer_lst

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]




class Song:
    tags = []

    def __init__(self, artist, song):
        self.artist = artist
        self.song = song

    def add_tags(self, *args):
        self.tags.extend(args)

song1 = Song('Shakey Graves', 'Roll the Bones')
print(song1.artist)
print(song1.song)
song1.add_tags('Americana', 'Country')
print(song1.tags)



















