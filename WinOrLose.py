def cal(villains, players):
    villains = [int(x) for x in villains]
    players = [int(x) for x in players]
    villains.sort()
    players.sort()

    isDefeated = True
    for i in range(len(villains)):
        if players[i] < villains[i]:
            isDefeated = False

    if isDefeated:
        print("WIN")
    else:
        print("LOSE")


cases = int(input())
vil = []
pla = []
for i in range(cases):
    vil.append(input())
    pla.append(input())

for i in range(len(vil)):
    cal(vil[i].split(),pla[i].split())

