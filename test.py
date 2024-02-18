print("hello world")


class carro:

    def __init__(self,motor, color, top_speed) -> None:
        self.motor = motor 
        self.color = color
        self.top_speed = top_speed

    
    def show_speed(self):
        print(self.top_speed)

    def show_color(self):
        print(self.color)


mazda = carro("v8", color="blue", top_speed=287)
mazda.show_color()