# Jonas Hallstrom 09/11/2024
# Plots for very important paper 

import matplotlib.pyplot as plt 
import numpy as np

data = np.genfromtxt("data.txt")
plt.plot(data, color="blue")
plt.savefig("Fig1A.png")
