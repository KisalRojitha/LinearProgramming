import numpy as np
import preProcessLP as lpModel
import display as krt


def solve(l):
    
    obj , obj_matrix ,constr_matrix , slackSurplas_matrix , Artifical_Matrix ,right_const_matrix =l
    #Simplex method 


    obj_matrix = -1* obj_matrix
    arr = np.concatenate((constr_matrix, slackSurplas_matrix), axis=1)
    arr = np.concatenate((arr, right_const_matrix), axis=1)

    temp = np.zeros((1,(len(arr[0])-len(obj_matrix[0]) ) ))
    obj_matrix = np.concatenate((obj_matrix, temp), axis=1)
    mat = np.concatenate((arr, obj_matrix), axis=0)

    titles = [constr_matrix, slackSurplas_matrix]
    print("Initial Tableau")
    krt.lpView1(mat,titles)



    #find the  index(i_enter) of the lowest value in the lowest row

    i_enter = mat[-1].tolist()
    c = [i for i in i_enter if i < 0]
    counter = 1
    while (len(c) != 0):
        if(len(c) != 0):
            i_enter = i_enter.index(min(c))
            print(i_enter)
            ratio=[]
            
            for i in range(len(mat)-1):
                d = mat[:,i_enter][i]
                if(d != 0):
                    rhs =mat[:,-1][i]
                    ratio.append( rhs / d )
             
            print("ratio " + str(ratio))

            c = [i for i in ratio if i >0]
            i_leave = 0
            if(len(c) != 0):
                i_leave = ratio.index(min(c))
            else:
                print("Work out here kisal... ")
                print("no postive values found but maybe zero exists which this not detected")

            print(i_leave)

            # divide pivot element by itself to get coffiexent 1

            mat[i_leave] = mat[i_leave]/mat[i_leave][i_enter]

            #print(mat)
            print("")

            # clean pivot col by row operations

            for i in range(len(mat)):
                d = mat[:,i_enter][i]
                if( i != i_leave and d != 0):
                    d = d *-1
                    mat[i] = mat[i] + mat[i_leave] * d

            print("Iteration " +str(counter))
            counter += 1
            temp = np.round(mat, 2)
            krt.lpView1(mat,titles)
            
            i_enter = mat[-1].tolist()
            c = [i for i in i_enter if i < 0]


        else:
            print("optimal solution  obtained or not obtained.still dont know")



    print("")
    print("finished .......................")
    print("optimal solution obtained  ")
