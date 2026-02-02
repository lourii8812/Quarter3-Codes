names = ["Lourence", "Liana", "Eonise", "Lezeth", "Chariena"]
expenses = [
  [120,  95, 150, 110, 130],  
  [200, 180, 220, 210, 190],  
  [ 85, 100,  90, 105,  95],  
  [160, 140, 155, 170, 165],  
  [110, 125, 115, 130, 120]  
]

print("Daily Expenses Report")
for name, daily_list in zip(names, expenses):
    amounts = []
    print(f"{name}'s Daily Expenses:")
    print("------------------------------")
    for day, amount in enumerate(daily_list, start = 1):
        print(f" Day{day}: {amount}", end=" ")
        amounts.append(amount)
    total = sum(amounts)
    average = total / len(amounts)
    print("\n-------------------------------")
    print(f"Total for {name}'s daily expenses: {total}")
    print(f"Average for {name}'s daily expenses: {average}")
    print("\n")
