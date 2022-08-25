class PlayerCharacter:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print('run')
        return 'done'
player_1=PlayerCharacter('asad',41)
# print(player_1.run())
# print(player_1.name,player_1.age)
player_1.run()
print(player_1.name,player_1.age)
