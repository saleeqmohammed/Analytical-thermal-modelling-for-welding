from matplotlib.pyplot import twinx
import numpy as np
#----------------------PLOT RESOLUTION:INCRESE THESE VALUES TO INCRESE PLOT RESOLUTION-------------------------------------------
res_x =50
res_y =100
res_z =70
#--------------------------------------------------------------------------------------------------------------------------------
twaiting=100
N_pass =2
# total time
twelding = 30
t = twelding +(N_pass)*(twelding+twaiting)
T0 = 303
a = 11.72
ah = 8.062
bh = 3.003
rf = 2/3 
rb = 4/3
chf = 7
chb =2*chf
v = 6.77
Tmelting = 1700
Tmelting_rel = Tmelting - T0
Source_voltage = 26
Source_current = 617
Source_efficiency = 0.92
rho = 7820*10**-9
c = 600
Q = Source_efficiency*Source_current*Source_voltage #power
x_range = np.linspace(-20,250,num = res_x )#229

y_range = np.linspace(-50,50,num = res_y)#49

z_range = np.linspace(-36,0,num = res_z)#35
