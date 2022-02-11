def climbingLeaderboard(ranked, player):
    ranks = []
    player.reverse()
    rank = 1
    i = 0
    j = 0
    while i < len(player) or j < len(ranked):
        if i < len(player) and j < len(ranked):
            if player[i] >= ranked[j]:
                ranks.append(rank)
                i += 1
            else:
                if j+1 < len(ranked):
                    if ranked[j] != ranked[j+1]:
                        rank += 1
                j += 1
        elif i >= len(player) and j < len(ranked):
            j+=1
        elif j >= len(ranked) and i < len(player):
            ranks.append(rank+1)
            i+=1    

    ranks.reverse()
    return ranks


ranked = list(map(int, input().rstrip().split()))
player = list(map(int, input().rstrip().split()))
result = climbingLeaderboard(ranked, player)
print(result)
