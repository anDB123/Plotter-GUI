import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(-1, 1, 500)
y = np.random.normal(-1, 1, 500)

fig, ax = plt.subplots()
ax.scatter(x, y, 50, "0.0", lw=2)
ax.scatter(x, y, 50, "1.0", lw=0)
ax.scatter(x, y, 40, "C1", lw=0, alpha=0.1)
plt.show()

# testing for commit working!!!
#last test I promise!
