import random


class Lion:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        one_index = random.randint(0, len(name))
        self.name = name[0:one_index] + '1' + name[one_index:]


class Zoo:
    def __init__(self):
        self.lions = {}

    def add_lion(self, lion):
        if not lion.name in self.lions:
            self.lions[lion.name] = lion
        else:
            # There was a problem because a lion with that name
            # already exists
            raise Exception("")

    def remove_lion(self, lion_name):
        if lion_name in self.lions:
            del self.lions[lion_name]

    def get_lions_amount(self):
        return len(self.lions)


if __name__ == '__main__':
    lion1 = Lion()
    lion1.set_name('Shlomi')
    print(lion1.name)
    lion2 = Lion()
    lion2.set_name('Robi')
    lion3 = Lion()
    lion3.set_name('Bobi')
    zoo = Zoo()
    zoo.add_lion(lion1)
    zoo.add_lion(lion2)
    zoo.add_lion(lion3)
    zoo.remove_lion('Robi')
    print(zoo.get_lions_amount())
