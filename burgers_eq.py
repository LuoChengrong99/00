import numpy as np
from math import pi
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab


params = {'legend.fontsize': 15,
          'legend.loc':'best',
          'figure.figsize': (14,5),
          'lines.markerfacecolor':'none',
         'axes.labelsize': 17,
         'axes.titlesize': 17,
         'xtick.labelsize':15,
         'ytick.labelsize':15,
         'grid.alpha':0.6}
pylab.rcParams.update(params)
#%matplotlib notebook
# %matplotlib inline

N=100
x=np.linspace(0,2*pi,N,endpoint=False)

u0 = np.sin(x)
# plt.figure(figsize=(14,5))
# plt.xlabel('x');plt.ylabel('u')
# plt.plot(x,u0,'-k',lw=2,label='initial condition')
# plt.legend(loc='best')
# plt.grid()

def FourMat(n):
    """ Fourier Matrix """    
    W=np.exp(-1j*2*pi/n)
    I,J=np.meshgrid(np.arange(n),np.arange(n))
    return (W**(I*J))
F=FourMat(N)/N
Finv=np.linalg.inv(F)

# you can use the DFT
# u0hh=F@u0
# or the FFT
u0hh=np.fft.fft(u0)/N

K=int(N/2)-1
u0hh[K+1]=0
u0h=np.fft.fftshift(u0hh) 

dt=0.01
nt=101
t=np.arange(nt)

kk=range(-K,K+1)

uh=u0h

for t_ in t:
    time=t_*dt
    f=0*uh
    for l_ in kk:
        
        for k_ in kk:
            m_=l_-k_
            if abs(m_)<=K:
                f[l_+int(N/2)] += 1j*m_*uh[k_+int(N/2)]*uh[m_+int(N/2)]
        
    uh = uh-dt*f
    
uhh=np.fft.ifftshift(uh)

# you can use the DFT
#u1=Finv@uhh  
# or the FFT
u1=np.fft.ifft(uhh*N)

    
plt.figure(figsize=(14,5))
plt.xlabel('x');plt.ylabel('u')
plt.plot(x,u0,'-k',label='initial condition')
plt.plot(x,u1.real,'-r',lw=2,label='$t=1$')
plt.legend(loc='best')
plt.grid()

plt.show()

print("good job") 