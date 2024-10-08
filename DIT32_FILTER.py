from cans import *
from cbc import *
from dit import *
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use('science')  # lines

folders = [
'DIT32_SMAG_CS0.18_FILTER/',
'DIT32_DSMAG_FILTER/',
# 'DIT32_SMAG_CS0.22_FILTER/',
]
labels = [
'SM',
'DSM',
# 'SM, $C_s=0.22$',
]

cbc = DIT('DIT32_SMAG_CS0.18_FILTER/')
cbc.read_spec()
plt.plot(cbc.generator.kappa, cbc.generator.energy0, label='CBC (box-filtered)', color='black')
plt.plot(cbc.generator.kappa, cbc.generator.energy1, color='black')
plt.plot(cbc.generator.kappa, cbc.generator.energy2, color='black')
for i in range(len(folders)):
  les = DIT(folders[i])
  les.read_spec()
  plt.plot(les.kappa, les.energy0, label=labels[i], color=f'C{i}')
  plt.plot(les.kappa, les.energy1, color=f'C{i}')
  plt.plot(les.kappa, les.energy2, color=f'C{i}')
plt.axvline(x=2*np.pi/(2*les.lx/les.nx), color='black', linestyle='--')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.xlabel('$\kappa (1/m)$')
plt.ylabel('$E(\kappa) (m^3/s^2)$')
plt.xlim([10, 1000])
plt.ylim([1e-6, 1e-3])
# plt.show()
plt.savefig(f"DIT32_FILTER.pdf", format='pdf', bbox_inches='tight')
plt.close()