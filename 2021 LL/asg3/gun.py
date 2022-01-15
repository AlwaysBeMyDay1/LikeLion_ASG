from weapon import Weapon

class Gun(Weapon):
    def __init__(self, weapon_name, power, bullet_num):
        super().__init__(weapon_name, power)
        self.bullet_num = bullet_num

    def attack(self):
        if self.bullet_num == 0:
            print('공격 불가!')
            return
        else:
            super().attack()
            self.bullet_num -= 1
            print('남은 총알 : ', self.bullet_num)
    
    def reload(self, num):
        self.bullet_num += num
        return self.bullet_num
