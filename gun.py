#Author:Jin
class Person:
    def __init__(self,name):
        self.blood=100
        self.name=name
        self.gun=None

    def __str__(self):
        return self.name+"剩余血量："+str(self.blood)

    def put_on_bullet(self,danjia,bullet):
        danjia.speichern(bullet)

    def add_in_danjia(self,gun,danjia):
        gun.link_with_danjia(danjia)

    def putgun(self,gun):
        self.gun=gun

    def kaiqiang(self,diren):
        self.gun.shook(diren)

    def injured(self,shashangli):
        self.blood-=shashangli

class Bullet:
    def __init__(self,shashangli):
        self.shashangli=shashangli

    def injured(self,diren):
        diren.injured(self.shashangli)

class Danjia:
    def __init__(self,contain):
        self.contain=contain
        self.bullet_num=[]

    def __str__(self):
        text="当前子弹数为："+str(len(self.bullet_num))+"/"
        text+=str(self.contain)
        return text

    def speichern(self,bullet):
        if len(self.bullet_num)<self.contain:
            self.bullet_num.append(bullet)

    def chuzidan(self):
        if len(self.bullet_num)>0:
            bullet=self.bullet_num[-1]
            self.bullet_num.pop()
            return bullet
        else:
            return None

class Gun:
    def __init__(self):
        self.danjia=None

    def __str__(self):
        if self.danjia:
            return "有弹夹"
        else:
            return "没有弹夹"

    def link_with_danjia(self,danjia):
        if not self.danjia:
            self.danjia=danjia

    def she(self,diren):
        bulet=self.danjia.chuzidan()
        if bullet:
            bullet.injured(diren)
        else:
            print("没有子弹")

class Sandan(Gun):
    def shook(self,diren):
        i=0
        while i<3:
            super().she(diren)  #父类调用加super-69
            i+=1

jin=Person("金")

gun=Sandan()
danjia=Danjia(20)
print(danjia)
i=0
while i<5:
    bullet = Bullet(5)
    jin.put_on_bullet(danjia,bullet)
    i+=1
print(danjia)
jin.add_in_danjia(gun,danjia)
diren=Person("敌人")
print(diren)
print("---------开始射击-----------")
jin.putgun(gun)
jin.kaiqiang(diren)
print(diren)
print(danjia)

