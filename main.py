data = "назва=Книга,автор=Шевченко,рік=1840"


dataa = data.split(',')

dict = {}

for i in dataa:
    key,elements = i.split('=')
    dict['b'] = elements

print(dict)
