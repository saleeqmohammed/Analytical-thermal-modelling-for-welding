from sys import implementation

from matplotlib.pyplot import vlines
from settings import*
import scipy.integrate as integrate
from math import *
import numpy as np

def integrand(tp,x,y,z):
    K =( 1/sqrt((( 12 * a * (t-tp) + ah**2)) * ((12*a*(t-tp) +bh**2)) ))
    A = rf*exp( ( -3*(x-v*tp)**2/(12*a*(t-tp)+chf**2)) - ( 3*y**2/(12*a*(t-tp)+ah**2)) - (3*z**2/(12*a*(t-tp)+bh**2)) )/(sqrt(12*a*t-tp)+chf**2)
    B = rb*exp( ( -3*(x-v*tp)**2/(12*a*(t-tp)+chb**2)) - ( 3*y**2/(12*a*(t-tp)+ah**2)) - (3*z**2/(12*a*(t-tp)+bh**2)) )/(sqrt(12*a*t-tp)+chb**2)
    return K*(A+B)

def calculate(el_time,x_range,y_range,z_range):
    calc_data = dict()
    for x in x_range:
        for y in y_range:
            for z in z_range:
                Tdiff = integrate.quad(integrand,0,el_time,args=(x,y,z))[0]*Q*5.19615/(2*rho*c*5.568328)*100
                coordinate =(x,y,z)
                calc_data[coordinate]=Tdiff
    return calc_data
def poolfilter(data):
    filterdata=dict()
    for key,value in data.items():
        if value >=Tmelting_rel:
            filterdata[key]=value
    return filterdata
def modifyrange(d_range,offset,axis):
    res=dict()
    for key,value in d_range.items():
        if axis=="y":
            up_key=(key[0],key[1]+offset,key[2])
            res[up_key]=value
        if axis=="x":
            up_key=(key[0]+offset,key[1],key[2])
            res[up_key]=value
    return res

def combinedata(things):
    res=dict()
    for item in things:
        for key,value in item.items():
            
            if key in res.keys():
                res[key]+=value
            else:
                res[key]=value
    return res
def ModifiedCombinedata(pools,Toffset):
    res = dict()
    
    for pool in pools:
        for key,value in pool.items():
            if( key[1] > -15 )and (key[1] < 25):
                res[key]=value+Toffset
            else:
                res[key] = value
    return res

def calculate_temporal(x,y,z,ti):
    t_range= np.linspace(0,ti,100)
    tempdata=[]
    for t in t_range:
        Tdiff = integrate.quad(integrand,0,t,args=(x,y,z))[0]*Q*5.19615/(2*rho*c*5.568328)*100
        tempdata.append(Tdiff+T0)
    return [t_range,tempdata]



    