def stringRead(a):

    if(a.find("Max") != -1 or a.find("max") != -1 or a.find("MAX") != -1):
        obj = "Max"
    elif(a.find("Min") != -1 or a.find("min") != -1 or a.find("MIN") != -1):
        obj = "Min"

     
    z_position = a.find("z")
    a=a[z_position:]
    x_found =False
    last_x = 0
    finish_index =0
    constraints = []
    constr =[]
    obj_func=""

    # find objective function

    for i in range(len(a)):
        
        if(a[i]=="x" and x_found ==True ):
         
            b = a[last_x:]
            finish_index = b.find(" ")
            finish_index = last_x+finish_index
            obj_func =a[0:finish_index+1]
            break;
        
        if(a[i]=="x" and x_found ==False ):
            x_found =True
            last_x = i
        if((a[i]=="+" or a[i]=="-") and a[i+1]==" "):
            x_found =False
        


    a=a[len(obj_func):]
    constraints = a.split(",")


    # clean the left and right of the constraints

    for b in constraints:
        for i in range(len(b)):
             if(b[i]==" " or b[i]=="\n" ):
                 c = b[i+1:]  
             else:
                 break;

        b = c[::-1] # reverse the string for remove right spaces and \n
        
        for i in range(len(b)):
             if(b[i]==" " or b[i]=="\n" ):
                 c = b[i+1:]
             else:
                 break;

        b = c[::-1]
        constr.append(b)
         
         

         
    # find number of variables in the objective function

    # firstly remove  upto '=' mark in objective function and clean left and right

    b = obj_func

    b = b[b.find("=")+1:]

    for i in range(len(b)):
             if(b[i]==" " or b[i]=="\n" ):
                 c = b[i+1:]
             else:
                 break;

    b = c[::-1] # reverse the string for remove right spaces and \n
        
    for i in range(len(b)):
        if(b[i]==" " or b[i]=="\n" ):
            c = b[i+1:] 
        else:   
            break;

    b = c[::-1]
    obj_func = b


    #find last x_index. it is the number of variables in the objective function

    varCount = obj_func.rfind("x")
    varCount = obj_func[varCount+1:]
    varCount = int(varCount)

    finalVar = [obj,obj_func ,constr , varCount ]


    return finalVar

def help():
    print("stringRead(lp_problem_string)")
    print("")
    print("return:")
    print("objective , objective function , constraints , variable count as a list")
    print("")
    print("Note:")
    print("")
    print("objective function must write like this z = 8x1 + 10x2 - 7x3 + 5x4 - 6x5 ")
    print("")
    
    print(""" Max z = 8x1 + 10x2 - 7x3 + 5x4 - 6x5


    -x1 + 3x2 + 2x3  <= 10 ,
    
    -2x1 - 5x2 -  x3  >= -8 ,
    
     x1 - 5x2 -  x3  >= 0  """  )
    
    print("")
    
    
    
    
    
    
