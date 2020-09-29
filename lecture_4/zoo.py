class Lion:
    def __init__(self, name, size, age):
        self.name = name
        self.size = size
        self.age = age


class Zoo:
    def __init__(self):
        self.lions = {}

    def add_lion(self, lion):
        self.lions[lion.name] = lion

    def remove_lion(self, lion_name):
        if lion_name in self.lions:
            del self.lions[lion_name]

    def get_lions_amonut(self):
        return len(self.lions)

if __name__ == '__main__':
    import pickle
    print(len(pickle.dumps(Lion('Hello',25,25))))