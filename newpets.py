class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.happiness = 5

    def eat(self):
        if self.happiness > 1:
            print(self.name + " picks up a McChicken, but he ain't eatin it, adios mio.")
        elif self.is_alive:
            print(self.name + " says 'This bizza is brackin'")
        else:
            print(self.name + " is too ded to eat lmao.")
            
    def fortnite(self):
        if self.is_alive:
            print(self.name + " says 'Where the heck we droppin fellas'")
        else:
            print(self.name + " is dead, WHAT DO YOU MEANNN????")

            
    def sleep(self):
        if self.is_alive:
            print(self.name + " is straight schlumped lmao")
        else:
            print(self.name + " is sleeping... 6 feet under XD")        

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self): 
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def kill(self, other):
        print(self.name + " discombobulates " + other.name +" and says '2 ez'")
        print(other.name + " goes 'MY LEG!' and dies.")
        other.is_alive = False

    def hug(self, other):
        if self.name == "Amber Rose":
            print(self.name + " hugs " + other.name +"!")
            other.happiness -= 1
            print(other.name + " says, 'BACK OFF YOU FIEND, NO THOTS!!'")
        else:
            print(self.name + " hugs " + other.name + "!")
            other.happiness += 1
            print(other.name + " says, 'OWO wats this ;)'")

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
pet1 = Pet("Lil Broomstick")
pet2 = Pet("Soulja Boy")
pet3 = Pet("Based God")
pet4 = Pet("Amber Rose")
