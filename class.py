# def generators():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#
# gen = generators()
# # print(type(gen))
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def func():
#     s = []
#     for i in range(1, 21):
#         s.append(i)
#     return s


# q = func()
# print((type(q)))
# print(func())
def fibo(n):
    a, b = 0, 1
    i = 0
    while i<n:
        yield a
        a , b = b, a+b
        i+=1
fibon = fibo(100)
for i in fibon:
    print(i)