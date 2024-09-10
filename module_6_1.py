class Animal:
    alive = True  # (живой)
    fed = False  # (накормленный)

    def __init__(self, name):
        self.name = name  # индивидуальное название каждого животного.

    def eat(self, food):
        if food.edible == True:
            if self.alive == True:
                print(f"{self.name} съел {food.name}")
                self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    edible = False  # (съедобность),
    def __init__(self, name):
        self.name = name  # индивидуальное название каждого растения

class Fruit(Plant):
    edible = True
class Flower(Plant):
    pass

class Mammal(Animal):
    pass
class Predator(Animal):
    pass


a1 = Predator('Серый волк')
a2 = Mammal('Оленёнок Бемби')
p1 = Flower('аленький цветочек')
p2 = Fruit('мешок яблок')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a1.eat(p2)     # волк на диете
a2.eat(p2)
print(a1.alive)
print(a2.fed)



