from functools import partial

'''def multiply(x, y):
    return x * y


# create a new function that multiply by 2
dbl = partial(multiply, 2)
print(dbl(4))'''


def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


# partial function
add_num = partial(func, 2, 10, 5)
print(add_num(12))
