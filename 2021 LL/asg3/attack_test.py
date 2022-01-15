import weapon
from gun import Gun
from knife import Knife

a = weapon.Weapon('몽둥이', 3)
b = Gun('M4', 3000, 2)
c = Knife('단검', 100, 2)

a.attack()
b.attack()
b.attack()
b.attack()
c.attack()
c.attack()
c.attack()