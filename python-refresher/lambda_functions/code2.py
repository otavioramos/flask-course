def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
print(doubled)

doubled2 = map(double, sequence)
print(list(doubled2))