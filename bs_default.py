import matplotlib.pyplot as plt
import numpy as np

energy_per_bs = []
nodes = []
for i in range(10):
    energy_per_bs.append(0)
    nodes.append(i)

with open('datasets/log_file_bs_basic_energy_consumption.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        energy_per_bs[int(l.split(',')[2])] = float(l.split(',')[-1].strip())

print(energy_per_bs)

plt.bar(nodes, energy_per_bs, width=0.4)
plt.xlabel('BS Nodes')
plt.ylabel('Energy (J)')
plt.xticks(np.array(nodes))
plt.show()