class PlayerCharacter:
    membership=True
    def __init__(self,name='asad',age=0):
        if age > 18:
            self.name=name
            self.age=age
        else:
            pass
    def shout(self):
        print(f'my name is {self.name}: and my age is {self.age}')
player_1=PlayerCharacter('asad',19)
player_2=PlayerCharacter()
print(player_1.shout())
