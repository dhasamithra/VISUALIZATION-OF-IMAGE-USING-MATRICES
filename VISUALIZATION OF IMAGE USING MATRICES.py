from tkinter import *
import matplotlib.pyplot as plt 

data = [
        [0,0,0,0,0,0,5,0],
        [0,0,0,0,0,9,5,0],
        [0,0,0,0,9,0,6,5],
        [0,0,0,9,0,0,6,5],
        [0,0,9,0,0,0,6,5],
        [0,9,0,0,0,0,6,5],
        [5,6,6,6,6,6,5,0],
        [0,5,5,5,5,5,0,0]]

plt.imshow(data, cmap="nipy_spectral")
plt.show()