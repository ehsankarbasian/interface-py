from interface_py import interface, concrete


@interface
class Human:
    def talk(self): pass
    def walk(self): ...


@interface
class MilitaryHuman(Human):
    # x: int
    # x = ...
    x: int = ...
    
    def shoot(self): ...


@concrete
class Commander(MilitaryHuman):
    x = 2
    
    def talk(self): print("talking")
    def walk(self): print("walking")
    def shoot(self): print("shooting")


# Raises error:
# Human()
# MilitaryHuman()

c = Commander()
c.talk()
print(c.x)
