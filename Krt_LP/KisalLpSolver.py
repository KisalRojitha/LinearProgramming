import os
import numpy as np
import preProcessLP as lpModel
import display as krt
import simplexMethod as lp




a = """

        Max z = 40x1 + 30x2 

            x1 + x2   <= 12 ,
    
            2x1 + x2  <= 16 
    
                         
                          
"""





l = lpModel.preProcess(a)
Artifical_Matrix  =l[4]
isArtificial = lpModel.checkArtificial(Artifical_Matrix,details=True)


if(isArtificial):
    pass
else:
    lp.solve(l)

  

os.system("pause")


