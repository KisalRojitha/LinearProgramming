import lpStringReader as lpstring
import oneLineMathExpression as Ex
import numpy as np


def ConvertToStandardForm(a):
    l = lpstring.stringRead(a)
    obj,obj_func,constr,varCount = l
    # print(obj_func)
    #a = np.array([[1, 2, 3],[3, 2, 1]])


    # covert constraints into three different matrix for coffieceient,comparison Sign , right side val

    constr_matrix = np.zeros((len(constr),varCount))
    right_const_matrix = np.zeros((len(constr),1))
    compSign_matrix = np.zeros((len(constr),1))

    for i in range(len(constr)):
        r=Ex.find_Constant(constr[i])
        s=Ex.find_Expression(constr[i],integer =True)
            
            
        right_const_matrix[i][0] = r
        compSign_matrix[i][0] = s
        for j in range(varCount):
            x= "x"+str(j+1)
            a = Ex.find_Xcoffiecient(x,constr[i])
            constr_matrix[i][j] = a
           
           
    # postive right side - standard formation no 1

    # check each value of the right_const_matrix, if negative multipli by -1
    # on coressponding line in each 3 matrices

    for i in range(len(right_const_matrix)):
        if(right_const_matrix[i] < 0):
            right_const_matrix[i] = right_const_matrix[i] * -1
            compSign_matrix[i] = compSign_matrix[i]* -1
            for j in range(len(constr_matrix[i])):
                constr_matrix[i][j] = constr_matrix[i][j] * -1



    #  initlize slack and surplace varialbe matrix 

    dim = len(constr_matrix)
    slackSurplas_matrix = np.zeros((dim,dim)) 

    # Add values
    for i in range(len(slackSurplas_matrix)):
  
        for j in range(len(slackSurplas_matrix[i])):
            if(compSign_matrix[i] in [-1,-2] ):
                if(i==j):
                    slackSurplas_matrix[i][j] = -1

                else:
                    slackSurplas_matrix[i][j] = 0
   
            elif(compSign_matrix[i] in [1,2]):
                if(i==j):
                    slackSurplas_matrix[i][j] = 1

                else:
                    slackSurplas_matrix[i][j] = 0

            else:
                slackSurplas_matrix[i][j] = 0
                
    # delete zeroth colonms in slackSurplas_matrix

    a = np.where(~slackSurplas_matrix.any(axis=0))
    for i in range(len(a[0])):
        b = np.where(~slackSurplas_matrix.any(axis=0))
        slackSurplas_matrix = np.delete(slackSurplas_matrix, b[0], axis=1) 
            
   
    #  convert objective function into the standard form
    
    
    obj_matrix = np.zeros((1,varCount))
    
    
    for j in range(varCount):
        x= "x"+str(j+1)
        a = Ex.find_Xcoffiecient(x,obj_func)
        if(obj =="Min"):
            obj_matrix[0][j] = -1*a
    
        else:
            obj_matrix[0][j] = a
   
    
    details = [obj , obj_matrix ,constr_matrix , slackSurplas_matrix , right_const_matrix]
    return details
    
    
def help():
    print("ConvertToStandardForm(string)")
    print("")
    print("Convert the lpstring in to a standard form return 5 type of values")
    print("[obj , obj_matrix ,constr_matrix , slackSurplas_matrix , right_const_matrix]")
    print("")
    print("not included artificial variables")
    print("slackSurplas_matrix need to optimize")
    
    

 
# l = ConvertToStandardForm(a)
# print(l)

