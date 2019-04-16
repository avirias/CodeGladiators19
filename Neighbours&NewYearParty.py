import collections as c


def cal(tickets):
    tickets = [int(x) for x in tickets]
    index = []
    pac = []
    maxim = tickets[0]
    for i in range(len(tickets)):
        maxi = tickets[i]
        packets = []
        index.clear()
        index.append(i)
        packets.append(tickets[i])
        for j in range(len(tickets)):
            if j not in [x + 1 for x in index] and j not in [x - 1 for x in index] and i != j:
                if maxi < maxi + tickets[j]:
                    maxi = maxi + tickets[j]
                    index.append(j)
                    packets.append(tickets[j])
            else:
                continue
        pac.append(packets)
        # print(packets)
        del packets
        # if sum(packets) not in [sum(x) for x in pac]:
        #     pac.append(packets)
        #
        if maxi > maxim:
            maxim = maxi
        # print(maxi)
    del index
    #
    # print(pac)
    # print(maxim)

    P = []
    for x in pac:
        if sum(x) == maxim and x not in P:
            P.append(x)
    del pac
    xam = [P[0]]
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if c.Counter(P[i]) != c.Counter(P[j]):
                xam.append(P[j])

    # print(xam)
    items = []
    for element in xam:
        element.reverse()
        items.append(element)
    del P
    maxItem = items[0]
    for i in range(len(items)):
        for j in range(len(items)):
            if maxItem[i] < items[j][i] and i != j:
                maxItem = items[j]
    for x in maxItem:
        print(x, end="")
    print()


cases = int(input())
nos = []
tic = []
for i in range(cases):
    nos.append(int(input()))
    x = [int(m) for m in input().split()]
    tic.append(x)
for x in tic:
    cal(x)
