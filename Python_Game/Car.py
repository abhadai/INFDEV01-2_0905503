class Car:
    def __init__(self, name, speed, pos_x, pos_y, sprite):
        self.Name = name
        self.Speed = speed
        self.PosX = pos_x
        self.PosY = pos_y
        self.Sprite = sprite

    def move(self, speed, direction):
        self.Speed = 5
        self.Direction = direction