def example_function(a, b='Default ff'):
    print(a)
    print(b)


class Ball:
    def __init__(self, radius, company, color):
        self.radius = radius
        self.company = company
        self.color = color
        self.x = 0
        self.y = 0

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def kick_x(self, v, t):
        self.x = self.x + v * t


class VolleyBall(Ball):
    def __init__(self, radius, company, color, is_for_beach):
        super().__init__(radius, company, color)
        self.is_for_beach = is_for_beach

    def move(self, new_x, new_y):
        if self.is_for_beach:
            self.x = new_x + 5
            self.y = new_y - 3
        else:
            super().move(new_x, new_y)
    def __add__(self, other):
        return VolleyBall(self.radius+other.radius,'Mizug','Red',False)

    def __str__(self):
        return "I'm a volley ball!"
vBall1 = VolleyBall(5, 'Diadora', 'Yellow', True)
vBall1.move(3, 3)
vBall2 = VolleyBall(5, 'Diadora', 'Yellow', True)
vBall2.move(4, 5)
vBall3 = vBall1 + vBall2
print(vBall3)
example_function(5, b='Shalom')
