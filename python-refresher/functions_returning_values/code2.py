def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return 'You fool!'


result = divide(divisor=0, dividend=15)
print(result)