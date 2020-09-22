import pickle


class Bird:
    def __init__(self, name, color, wing_size):
        self.name = name
        self.color = color
        self.wing_size = wing_size
        self.food = 0

    def add_food(self, food_amount):
        self.food += food_amount

    def __str__(self):
        return self.name + " " + self.color + ' ' + str(self.food)


# bird = Bird('Ethan', 'Red', 5)
# bird.add_food(10)
# print(bird)
# with open('bird_file.bin', 'wb') as f:
#     pickle.dump(bird, f)
with open('bird_file.bin', 'rb') as f:
    bird = pickle.load(f)
bird.add_food(5)
print(bird)
