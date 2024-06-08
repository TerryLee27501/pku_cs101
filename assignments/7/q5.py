t = int(input())
members = [0] * 1000000
teams = [[] for _ in range(t)]
team_order = []
for i in range(t):
    team_members = list(map(int, input().split()))
    for member in team_members:
        members[member] = i


def enqueue(member):
    team = members[member]
    teams[team].append(member)
    if team not in team_order:
        team_order.append(team)


def dequeue():
    first_team = team_order[0]
    print(teams[first_team].pop(0))
    if not teams[first_team]:
        team_order.pop(0)


while True:
    raw = input()
    if raw[0] == 'E':
        enqueue(int(raw[8:]))
    elif raw[0] == 'D':
        dequeue()
    else:
        break