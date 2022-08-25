class PlayerCharacter:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        return 'run'
    def speak(self):
        print(f'hey my name is {self.name} and i am {self.age} years old')
player_1=PlayerCharacter('ahmad',19)
player_1.name='ali'
player_1.age=20
print(player_1.speak() )