import matplotlib.pyplot as plt
import numpy as np

def plot_horizontal_trig(x_1):
    #create a range of x values from 0 to 2pi
    x = np.linspace(x_1[0], x_1[1], 1000)

    #define function
    y_1 = np.sin(x) 
    y_2 = np.cos(x)

    fig, axes = plt.subplots(1, 2, figsize=(12, 7))
    axes[0].plot(x, y_1, label="sin(x)", color="pink")
    axes[0].set_title("sin(x)")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("sin(x)")
    axes[0].legend()
    axes[0].grid(True)
    
    axes[1].plot(x, y_2, label="cos(x)", color="green")
    axes[1].set_title("cos(x)")
    axes[1].set_title("cos(x)")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("cos(x)")
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    fig.suptitle("horizontal")
    plt.show()


def plot_vertical_trig(x_1):
    #create a range of x values from 0 to 2pi
    x = np.linspace(x_1[0], x_1[1], 1000)

    #define function
    y_1 = np.sin(x) 
    y_2 = np.cos(x)

    fig, axes = plt.subplots(2, 1, figsize=(12, 7))
    axes[0].plot(x, y_1, label="sin(x)", color="pink")
    axes[0].set_title("sin(x)")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("sin(x)")
    axes[0].legend()

    
    axes[1].plot(x, y_2, label="cos(x)", color="green")
    axes[1].set_title("cos(x)")
    axes[1].set_title("cos(x)")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("cos(x)")
    axes[1].legend()
   

    plt.tight_layout()
    fig.suptitle("vertical subplots")
    plt.show()

