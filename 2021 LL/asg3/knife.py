from weapon import Weapon

class Knife(Weapon):
    def __init__(self, weapon_name, power, durability) :
        super().__init__(weapon_name, power)
        self.durability = durability

    def attack(self):
        if self.durability == 0:
            print('공격 불가!')
            return
        else:
            super().attack()
            self.durability -= 1
            print('내구성 : ', self.durability)