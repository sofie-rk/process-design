# Hold tank

import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt

def cstr(x, t, xin=1000, tau=11.1):
    '''
    Inputs:
        x:      mole-fraction array (needed for odeint)
        t:      t-values array (needed for odeint)

        xin:    inlet mole fraction
        tau:    residence time

    Outputs:
        right hand side of the ODE: 
        dx/dt = (x_in - x)/tau
    '''
    return (xin - x[0]) / tau 

xin = 1000
time_end = 0.5                              # leak for 0.5 hour
t_interval = np.linspace(0, time_end)       # [hours]
x0 = np.array([100])                        # initial condition


# odeint takes in:  cstr:   right hand side of the ODE
#                   x0:     initial value
#                   t:      t-values for evaluation
# odeint return:    array of x-values, corresponding to t-values

x_values = odeint(cstr, x0, t_interval)

# Max x is at the end of the leak (last x-value)
x_max = x_values[-1][0]
x_max_text = "Max x(t) = " + str(round(x_max,1)) + "ppm"


plt.plot(t_interval, x_values, label="x(t) [ppm]")
plt.plot(time_end, x_max, "ro", label=x_max_text)
plt.plot(t_interval, [x_max for i in range(len(t_interval))], "--", color="red")
plt.xlabel("t [hours]")
plt.ylabel("x(t)")
plt.legend()
plt.show()
 