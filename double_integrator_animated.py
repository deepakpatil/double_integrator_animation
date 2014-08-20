

from numpy import array
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation


def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]
    if (state[0]+state[1]*abs(state[1])/2)>0:
           dydx[1] = -1
    else:
         dydx[1] = 1


    dydx[2] = state[3]


    if (state[2]+state[3]*abs(state[3])/2)>0:
           dydx[3] = -1
    else: 
         dydx[3] = 1

    return dydx

# create a time array from 0..100 sampled at 0.1 second steps
dt = 0.005
t = np.arange(0.0, 10, dt)


x = 1.9
xdot = 1.0
y= 1
ydot = 2.0


# initial state
state = np.array([x, xdot, y, ydot])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = y[:,0]
y1 = y[:,1]

x2 = y[:,2] 
y2 = y[:,3]

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-8,8), ylim=(-8, 8))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    thisx = [ x1[i],x1[i]]
    thisy = [ x2[i],x2[i]]

    line.set_data(thisx,thisy)
    time_text.set_text(time_template%(i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
    interval=25, blit=True, init_func=init)

ani.save('double_integrator.mp4', fps=15, clear_temp=True)
plt.show()
