lst:list[int] = [1,2,3,4,5]

el:list[int] = lst[::-1]

el.insert(len(lst),99)
print(el)

el.pop(2)
print(el)

el.pop()
print(el)