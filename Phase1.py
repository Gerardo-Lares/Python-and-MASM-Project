import math
from matplotlib import pyplot as plt

# Sets the size of the window
plt.figure(figsize=(8,8))

# Setting up the axes we will be drawing on
tStart = 2005.0
tStop = 2010.0
fStart = 400.0
fStop = 700.0
plt.axis([tStart, tStop, fStart, fStop])
plt.ylabel('f', fontsize=20)
plt.xlabel('t', fontsize=20)
plt.title('Direction Fields', fontsize=20)

def differentialEquation(f, t):
    """This is the differential equation that will generate the DF"""
    return( 0.3 * (500 - f) * math.exp(t))

# Grid step size
gridt = 1.0
gridf = 1.0
dt = gridt

t = tStart
while t <= tStop:
    f = fStart
    while f <= fStop:
        plt.plot([t], [f], 'ko', ms = 2.0)
        df = differentialEquation(f,t)*dt
        length = math.sqrt(df*df + dt*dt) #makes the arrows have a length of the t grid
        vectorScaling = 0.7*(dt/length) # This will scale the vectors so they will be 0.7 the length of the t grid step.
                                        # This makes a pretty picture. Set it to 1 for a true vector strength picture.
        plt.arrow(t, f, dt*vectorScaling, df*vectorScaling, head_width=0.04, head_length=0.08, fc='g', ec='purple')
        f += gridf
    t += gridt

plt.show()
