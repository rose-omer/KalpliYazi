import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 100)
x = 16*np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

plt.plot(x, y, 'r')
plt.text(0, -2, 'Seni Seviyorummm \n AŞKIMMM  ', fontsize=20, fontweight='bold', color='blue', ha='center')
plt.axis('equal')
plt.axis('off')
plt.show()