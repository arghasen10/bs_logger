import matplotlib.pyplot as plt
import numpy as np

energy_per_ue = []
nodes = []
for i in range(10):
    energy_per_ue.append(0)
    nodes.append(i)

with open('datasets/log_file_ue_basic_energy_consumption.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        energy_per_ue[int(l.split(',')[1][-1])] = float(l.split(',')[-1].strip())

print(energy_per_ue)

plt.bar(nodes, energy_per_ue, width=0.4)
plt.xlabel('UE Nodes')
plt.ylabel('Energy (J)')
plt.xticks(np.array(nodes))
plt.show()