import numpy as np
names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
steps =[
[4500, 5200, 4800, 5000, 5300],
[4000, 4100, 3900, 4200, 4600],
[6000, 5800, 5900, 6100, 6200]
]
maxsteps = 0
def sum_column_numpy(two_d_array, column_index):
    np_array = np.array(two_d_array)
    return np_array[:, column_index].sum()
for i in range(len(steps[1])):
    x = i
    result = sum_column_numpy(steps, i)
    print(f"The total steps for {days[i]} is: {result}")
    if result > maxsteps:
        maxsteps = result
        activeday = days[i]
print(f"The most active day is {activeday} with {maxsteps} steps.")
