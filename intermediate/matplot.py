print(year[-1])
print(pop[-1])

import matplotlib.pyplot as plt

plt.plot(year, pop)
plt.show()

plt.scatter(gdp_cap, life_exp)
plt.xscale('log') # Put the x-axis on a logarithmic scale
plt.show()