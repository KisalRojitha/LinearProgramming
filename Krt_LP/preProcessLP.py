import standardForm as stdForm
import numpy as np


def preProcess(a):
    l = stdForm.ConvertToStandardForm(a)
    obj , obj_matrix ,constr_matrix , slackSurplas_matrix , right_const_matrix = l

    arr = np.concatenate((constr_matrix, slackSurplas_matrix), axis=1)

    # identifiying Artifical variables

    arr2 = np.zeros((len(arr),len(arr[0])))
    #this check elements in each row and  check  wether their particular coloumn's only value is itself only
    tempj = 0
    for i in range(len(arr)):
        basic_found =False
        for j in range(len(arr[i])):
            if(arr[i][j] != 1):
                
                continue
            else:
                
                for k in range(len(arr)):
                    if(arr[k][j] != 0 and k != i):
                        
                        break
                    
                    if(k == len(arr)-1):
                        basic_found =True         
          
        if(basic_found == False):
            arr2[i][tempj]=1
            tempj = tempj+ 1
             
             
    # delete zeroth colonms in Artifical_Matrix

    a = np.where(~arr2.any(axis=0))
    for i in range(len(a[0])):
        b = np.where(~arr2.any(axis=0))
        arr2 = np.delete(arr2, b[0], axis=1) 

    Artifical_Matrix = arr2
    
    l = [obj , obj_matrix ,constr_matrix , slackSurplas_matrix , Artifical_Matrix ,right_const_matrix]
    return l 


def checkArtificial(Artifical_Matrix,details=False):
    if Artifical_Matrix.size == 0:
        if(details ==True):
            print("No Artifical Variables Available... ")
            print("")
            print("Proceeding to simplex Method...")
            print("")
            print("")
        return False
        
    else:
        if(details ==True):
            print("Artifical variables exist")
            print("")
            print("Proceeding to Two Phase Method Method...")
            print("")
            print("")
        return True
        

def checkBasicPos(arr):
    arr2 = []
        #this check elements in each row and  check  wether their particular coloumn's only value is itself only
    for i in range(len(arr)):
        basic_found =False
        for j in range(len(arr[i])):
            if(arr[i][j] != 1):
                
                continue
            else:
                
                for k in range(len(arr)):
                    if(arr[k][j] != 0 and k != i):
                        
                        break
                    
                    if(k == len(arr)-1):
                        basic_found =True
                        xy = []
                        xy.append(i)
                        xy.append(j)
                        arr2.append(xy)
    return arr2
                

def help():
    print("preProcess(a)")
    print("checkArtificial(Artifical_Matrix,details=False)")
    print("checkBasicPos(matrix)")
    print("")
    print("checkBasicPos checks basic colounm and return list of coordinates of 1's position in each colounm")
    