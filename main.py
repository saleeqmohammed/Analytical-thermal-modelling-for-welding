import math

from matplotlib.pyplot import plot
import mathmodel
import plotter
import datamanagement
from settings import *
if __name__=="__main__":
    #pass1data=mathmodel.calculate(30,[0],y_range,z_range)
    #datamanagement.save_object(pass1data,"pass1data")
    '''
    def multipassyz(N_pass):
        result=[]    
        for i in range(N_pass):
            filename="pass"+str(i+1)+"data"
            try:
                est=datamanagement.load_object(filename+".pickle")
                est=mathmodel.modifyrange(est,i*20,"y")
                result.append(est)
            except:
                est = mathmodel.calculate(30+i*twaiting,[0],y_range,z_range)
                est=mathmodel.modifyrange(est,i*20,"y")
                result.append(est)
                datamanagement.save_object(est,filename)

        result=mathmodel.combinedata(result)
        plotter.weld_plot("space-temperature",result)
    try:
        step1=datamanagement.load_object("step1.pickle")
        step2=datamanagement.load_object("step2.pickle")
    except:
        step1=mathmodel.calculate(30,x_range,y_range,z_range)
        step1=mathmodel.poolfilter(step1)
        step2=mathmodel.modifyrange(step1,50,"x")
        datamanagement.save_object(step1,"step1")
        datamanagement.save_object(step2,"step2")
    result=mathmodel.combinedata([step1,step2])
    plotter.plot3D(result)
    '''
    N_pass=10
    result=[]
    for i in range(N_pass):

            filename="step1"
            try:
                est=datamanagement.load_object("step1.pickle")
                est=mathmodel.poolfilter(est)
                est=mathmodel.modifyrange(est,70*i,"x")
                
                result.append(est)
            except:
                est = mathmodel.calculate(30+i*twaiting,x_range,y_range,z_range)
                datamanagement.save_object(est,filename)
                est=mathmodel.poolfilter(est)
                est=mathmodel.modifyrange(est,20*i,"x")
                result.append(est)
                

    result=mathmodel.combinedata(result)
    plotter.plot3D(result)
        
