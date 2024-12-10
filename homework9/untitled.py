#create a range of x values from -2pi to 2pi
#start, stop, step is the pattern for np.linspace
x_data = np.linspace(0, 2 * np.pi, 1000)

#define function
y_1 = np.sin(x) 
y_2 = np.cos(x)

# plot the trig functions
plt.plot(x, y_1, label="sinx", color="green")
plt.plot (x, y_2, label="sinx")
plt.legend(loc="upper right", bbox_to_anchor=(1.5, 1))
plt.show() # ensures we actually see graphed stuff

fig, ax = plt.subplots(2, 2, figsize=(10,10))
ax[0,1].plot(x, y_1)
ax[1,1].plot(x, y_2)

# you can loop through your subplots
for i, ax in enumerate(ax.flat):
    ax.set_title(f"Frame{i}")
plt.show()