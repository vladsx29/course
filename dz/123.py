data = [
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    ['н', 'л', 'о', 'с']
]

data[0].reverse()
first = data[1].pop(0)
last = data[1].pop(-1)
data[1].insert(0, last)
data[1].append(first)
first = data[2].pop(0)
last = data[2].pop(-1)
data[2].insert(0, last)
data[2].append(first)
print(data)