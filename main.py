nested_list =[
    ['a', 'b',['sdf',888,{'sdf':['123',333]}], 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],'wer',[111]
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


class FlatIteratorV2:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.iterators_stack = [iter(self.multi_list)]  # стэк итераторов
        return self

    def __next__(self):
        while self.iterators_stack:  # пока в стеке есть итераторы
            # print(self.iterators_stack)
            try:
                current_element = next(self.iterators_stack[-1])
                #  пытаемся получить следующий элемент
            except StopIteration:
                self.iterators_stack.pop()
                continue
            if isinstance(current_element, list):
                # если следующий элемент оказался списком, то
                # добавляем его итератор в стек
                self.iterators_stack.append(iter(current_element))
            else:
                # если элемент не список, то просто возвращаем его
                return current_element
        raise StopIteration

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
        if type(items) != list:
            yield items
        else:
            for item_ in FlatGenerator2(items):
                yield item_



if __name__ == '__main__':
    # print(FlatIteratorV2(nested_list))
    # for item in FlatIteratorV2(nested_list):
    #     print(item)
    fl_list = [item for item in FlatIteratorV2(nested_list)]
    print(fl_list)
    # #
    # # list2 = [['sdf','qwe'],23,56,78,89]
    #
    # for i in FlatGenerator2(nested_list):
    #     print (i)
    # dik = {k:v for k,v in enumerate(FlatGenerator2(nested_list))}
    # print (dik)