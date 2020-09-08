def gen_x():
    n=1
    print("Printing 1")
    yield n

    n+=1
    print("Printing 2")
    yield n
    n+=1
    print("Printing 3")
    yield n


gen=gen_x()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))