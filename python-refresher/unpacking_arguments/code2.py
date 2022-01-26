def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))

# ----------------

nums2 = {'x': 15, 'y': 25}
print(add(**nums2))