import datetime
import requests
from pprint import pprint

class MyRange:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __iter__(self):
        self.cursor = self.start - 1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= self.finish:
            raise StopIteration
        return self.cursor

class MyDateRange:
    def __init__(self, start, finish):
        self.start = start - datetime.timedelta(days=1)
        self.finish = finish

    def __iter__(self):
        self.cursor = self.start
        return self

    def __next__(self):
        self.cursor += datetime.timedelta(days=1)
        if self.cursor >= self.finish:
            raise StopIteration
        return self.cursor

class SW_Basic:
    next_page = ''
    def __init__(self):
        pass

    def __iter__(self):
        # self.next_page = 'https://swapi.dev/api/people/'
        self.curent_result = []
        return self

    def __next__(self):
        print (self.next_page)
        if not self.curent_result:
            if not self.next_page:
                raise StopIteration
            res = requests.get(self.next_page).json()
            self.next_page = res['next']
            print ()
            self.curent_result = [res['results']]
        return self.curent_result.pop() # .pop() возвращает и удаляет посл. элемент в списке

class SW_people(SW_Basic):
    next_page = 'https://swapi.dev/api/people/'

class SW_starship(SW_Basic):
    next_page = "https://swapi.dev/api/starships/"

for item in MyDateRange(datetime.date(2022,9,25),datetime.date(2022,10,3)):
    print(item)

# res = requests.get('https://swapi.dev/api/people/')
# pprint(res.json())
#
# res = requests.get('https://swapi.dev/api/people/').json()
# pprint((res))
#
for people in SW_starship():
   pprint(people)