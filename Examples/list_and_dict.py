from typing import Dict

a = []
for i in range(10, 20):
    a.append(i)

for i in a:
    sample: Dict = {i: "number"}
    print(sample)

b = []
for i in range(20, 30):
    b.append(i)
output: Dict = {"barcilona": b}
print(output)

win = []
loss = []
team_name = input("Enter the team name: ")

for i in range(10, 30):
    win.append(i)

for j in range(10, 30):
    loss.append(j)

output_1 = [win, loss]
result: Dict = {team_name: output_1}
print(result)

start = int(input("enter the start range: "))
end = int(input("enter the start range: "))

x = []
for i in range(start, end):
    winning_percentage = int(input("Enter the winning percentage: "))
    x.append(winning_percentage)
print(x)

for i in range(10, 20):
    team = input("enter the team name: ")
    winning = int(input("enter the winnings: "))
    sample_output: Dict = {team: winning}
print(sample_output)

