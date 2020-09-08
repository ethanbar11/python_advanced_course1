lst = [i for i in range(100)]

iterat = iter(lst)
# Option 1
# while True:
#     print(iterat.__next__())

# Option 2
for i in range(100):
    print(next(iterat))
