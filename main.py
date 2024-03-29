#author: Mohammed saleeq K
#!/bin/env/python3
import math

from matplotlib.pyplot import plot
import mathmodel
import plotter
import datamanagement
from settings import *
if __name__=="__main__":
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

