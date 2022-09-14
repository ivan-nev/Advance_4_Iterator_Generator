class Peopl:
    living = 'Russia'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def what_is_self(self):
        return self

    def __str__(self):
        return f'{self.name} - {self.age} - {self.living}'

misha = Peopl('misha',35)
vas = Peopl('vas',3)
print((misha.what_is_self()))
print((vas.what_is_self()))


def A(n):
    if(n>=1):
        A(n-1)
        print(n)

A(10)

nested = [1,2,3,[33,['sdf','wer'],45,67]]
def Flatgenerator(nested):
    for items in nested:
        if isinstance(items, list):
            # print('+')
            Flatgenerator(items)
        yield (items)

for i in Flatgenerator(nested):
    print(i)


for k,v in enumerate([555,666,777]):
    print (k,v)

dik = {k:v for k,v in enumerate([555,666,777])}
print (dik)