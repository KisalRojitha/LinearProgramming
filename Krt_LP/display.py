import numpy as np
from tabulate import tabulate
import preProcessLP as lpModel

def addRowTitles(table ,col1):
    table = table.tolist()
    final_table =[]

    for i in range(len(table)):
        line=[]
        temp=[]
        temp.append(col1[i])
        line = temp + table[i]
        final_table.append(line)
        
    return final_table


def lpTable(table ,col1 , headers):
     final_table = addRowTitles(table ,col1)   
     print(tabulate(final_table,headers ,tablefmt="fancy_grid"))
    


def lpView1(mat,titles,raw =False):
    # in this no Ratio will be there
    constr_matrix,slackSurplas_matrix= titles
    s= np.array(mat[:len(mat),:len(mat[0])-1])
    k =lpModel.checkBasicPos(s)
    header = []
    for i in range(len(constr_matrix[0])):
        x= "x"+str(i+1)
        header.append(x)
    for i in range(len(slackSurplas_matrix[0])):
        x= "s"+str(i+1)
        header.append(x)    
    basicVar =[]
    for p in k:
       basicVar.append(header[p[1]])
    
    header.append("R.H.S")
    basicVar.append("z")
    
       
    lpTable(mat ,basicVar , header)    

    
    
def help():
    print(" addRowTitles(table ,col1_title)")
    print("    add row description to a table and return a list")
    
    print("")
    print(" addRowTitles(table ,col1_title)")
    print("    Print a table with colounm title and with row desctiption")


# headers=["x1","x2","x3"]
# col1 =["row1","row2","row3"]
# table = np.zeros((3,3))
# 
# 
# 
# lpTable(table,col1,headers)

 
