import math
from matplotlib import pyplot as plt
import mathmodel
import plotter
import datamanagement
from settings import *
if __name__=="__main__":
    #pass1data=mathmodel.calculate(30,[0],y_range,z_range)
    #datamanagement.save_object(pass1data,"pass1data")

    def multipassyz(N_pass):
    
        result=[]    
        for i in range(N_pass):

            el_time=t-i*(twelding+twaiting)
            print(el_time)
            est = mathmodel.calculate(el_time,[0],y_range,z_range)
            est=mathmodel.modifyrange(est,i*20,"y")
        
            result.append(est)
               # datamanagement.save_object(est,filename)

        #result=mathmodel.ModifiedCombinedata(result,0)
        result =  mathmodel.combinedata(result)
        
        plotter.weld_plot("space-temperature",result)
    multipassyz(2)
