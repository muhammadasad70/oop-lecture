class PlayerCharacter:
    membership=True
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def shout(self):
        print(f'my name is {self.name}: and my age is {self.age}')
    @classmethod
    def adding_things(cls,num_1,num_2):
        return cls('asad',num_1+num_2)
    @staticmethod
    def adding_things2(num_1,num_2):
        return num_1+num_2


player_1=PlayerCharacter('asad',19)
player_2=PlayerCharacter('ahmad',23)
# print(player_1.adding_things(2,3))
player_3=PlayerCharacter.adding_things2(10,15)
print(player_3.age)