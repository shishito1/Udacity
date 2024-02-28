import numpy as np
import matplotlib.pyplot as plt

x_rand = np.random.normal(0, 0.1, size=(1000, 1000))

plt.plot(x_rand)

# save then show plot locally
plt.savefig('normal_random_plot2.jpg')
plt.show()
