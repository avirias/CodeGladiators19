def cal(villans,players):
    villans = [int(x) for x in villans]
    players = [int(x) for x in players]
    villans.sort()
    players.sort()

    isDefeated = True
    for i in range(len(villans)):
        if players[i] < villans[i]:
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

