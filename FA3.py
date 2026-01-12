names = ["Lourence", "Liana", "Eonise", "Lezeth", "Chariena"]

expenses = [
    [120,  95, 150, 110, 130],
    [200, 180, 220, 210, 190],
    [ 85, 100,  90, 105,  95],
    [160, 140, 155, 170, 165],
    [110, 125, 115, 130, 120]
]
#Code:
totaloverall = 0
weekly_totals = []
maxz = 0
gastador = ""
for i in range(len(names)):
    total_spent = sum(expenses[i])
    weekly_totals.append(total_spent)
    totaloverall += total_spent
    print(f"{names[i]} spent ₱{total_spent} this week.")
averagespent = totaloverall / len(names)
print(f"\nAverage spent this week: ₱{averagespent}")
for i in range(len(expenses)):
    for value in expenses[i]:
        if value > maxz:
            maxz = value
            gastador = names[i]
print(f"Max amount spent on a day by a person was ₱{maxz} by {gastador}")
