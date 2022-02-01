#Parent class with a method 
class Bird:
    Wings = 2
    Flight = True
    Climate = ""
    def intro(self):
       print("There are different types of birds")
 
    def flight(self):
       print("Most of the birds can fly but some cannot")

#Child class 1 
class parrot(Bird):
    Flight = True
    Climate = "Warm"
    Talking = True 
    def flight(self):
       print("Parrots can fly")
 
#Child Class 2 
class penguin(Bird):
    Flight = False
    Climate = "Cold"
    Number_of_Mates = 1
    def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()
