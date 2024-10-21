#self == this

class Pizzera():
    code = 0
    high = 0
    diameter = 0
    material = " "

    def volume(self):
        print("Pizzera volume: ", 3.14*(self.diameter/2)*2*self.high)

class Glass():
    code = 0
    high = 0
    diameter = 0
    material = " "

    def volume(self):
        print("Glass volume: ", 3.14*(self.diameter/2)*2*self.high)

class Pot():
    code = 0
    high = 0
    diameter = 0
    material = " "

    def volume(self):
        print("Pot volume: ", 3.14*(self.diameter/2)*2*self.high)

#Pizzeras

pizzeras = []
for i in range(5):
    p = Pizzera()
    p.code = i + 1
    p.high = 2
    p.diameter = 30
    p.material = "Steel"
    pizzeras.append(p)
    p.volume()

# Vasos

g1 = Glass()
g1.code = 1
g1.high = 10
g1.diameter = 5
g1.material= "Glass"
g1.volume()

g2 = Glass()
g2.code = 2
g2.high = 15
g2.diameter = 5
g2.material= "Glass"
g2.volume()

g3 = Glass()
g3.code = 3
g3.high = 15
g3.diameter = 4.5
g3.material= "Glass"
g3.volume()


g4 = Glass()
g4.code = 4
g4.high = 10
g4.diameter = 4.5
g4.material= "Plastic"
g4.volume()

g5 = Glass()
g5.code = 5
g5.high = 10
g5.diameter = 5
g5.material= "Glass"
g5.volume()

# Ollas
pt1 = Pot()
pt1.code = 1
pt1.high = 20
pt1.diameter = 40
pt1.material= "Steel"
pt1.volume()

pt2 = Pot()
pt2.code = 2
pt2.high = 5
pt2.diameter = 15
pt2.material= "Aluminum"
pt2.volume()

pt3 = Pot()
pt3.code = 3
pt3.high = 15
pt3.diameter = 20
pt3.material= "Mud"
pt3.volume()

pt4 = Pot()
pt4.code = 4
pt4.high = 10
pt4.diameter = 25
pt3.material= "Copper"
pt4.volume()

pt5 = Pot()
pt5.code = 5
pt5.high = 25
pt5.diameter = 35
pt5.material= "Ceramics"
pt5.volume()