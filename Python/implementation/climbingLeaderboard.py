def climbingLeaderboard(ranked, player):
    # Write your code here
    ranks = []
    ranked = sorted(list(set(ranked)),reverse=True)
    for i in range(len(player)):
        ranked.append(player[i])
        ranked = sorted(list(set(ranked)),reverse=True)
        rank = ranked.index(player[i])
        ranks.append(rank + 1)
    print(ranks)
    return ranks


ranked = list(map(int, input().rstrip().split()))
player = list(map(int, input().rstrip().split()))

result = climbingLeaderboard(ranked, player)

