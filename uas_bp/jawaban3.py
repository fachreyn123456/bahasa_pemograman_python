import matplotlib.pyplot as plt
plt.plot()

plt.plot([10,15,20,25,30,35,40,45,50])
plt.show()

import numpy as np
x = [10,15,20,25,30,35,40,45,50]
y = np.array(x)**2

plt.plot(x,y)
plt.xlabel('sumbu x')
plt.ylabel('sumbu y')
plt.title('grafik')
plt.show()

plt.subplot(121)
plt.plot(x,y,color = 'LightBlue')
plt.xlabel('sumbu x')
plt.ylabel('sumbu y')

plt.subplot(122)
plt.plot(x,y,color = 'DarkBlue')
plt.xlabel('sumbu x')
plt.ylabel('sumbu y')
plt.tight_layout()
plt.show()
