nested_list = [
    ['a', 'b',['sdf',888,{'sdf':['123',333]}], 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],'wer'
]



class FlatIterator:
    def __init__(self, nested_list):
        self.flat_list = Flat_List(nested_list)

    def __iter__(self):

        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor >= len(self.flat_list):
            raise StopIteration
        self.cursor += 1
        return self.flat_list[self.cursor-1]

def Flat_List(nested_list):
    temp_list = []
    while True:
        if any(isinstance(i, list) for i in nested_list): # проверка есть ли вложенные списки
            for i in nested_list:
                if isinstance(i, list):
                    temp_list.extend(i)
                else:
                    temp_list.append(i)
            nested_list = temp_list
            temp_list = []
        else:
            return nested_list


def FlatGenerator(nested_list):
    for items in Flat_List(nested_list):
        yield items

# как сделать через рекурсию?
def FlatGenerator2(nested_list):
    for items in nested_list:
        if isinstance(items, list):
           print('+')
           FlatGenerator2(items)
           yield items



if __name__ == '__main__':
    print(FlatIterator(nested_list))
    for item in FlatIterator(nested_list):
        print(item)
    fl_list = [item for item in FlatIterator(nested_list)]
    print(fl_list)
    #
    # list2 = [['sdf','qwe'],23,56,78,89]

    for i in FlatGenerator(nested_list):
        print (i)
