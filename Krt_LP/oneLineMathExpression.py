
def find_Xcoffiecient(name,func,integer=False): # variable is x 
    
    if(name=="x1" and func.find(name)!= -1):
        z = func.find(name)
        val = func[:z]
        if(val=="" or val =="+"):
            val = "1"
        elif( val == "-"):
            val = "-1"
    else:
        if(func.find(name)!= -1):
            z = func.find(name)
            val = func[:z]
            
            rightMostSignPlus = val.rfind("+")
            rightMostSignMinus= val.rfind("-")
            if(rightMostSignPlus > rightMostSignMinus):
                z =rightMostSignPlus
            else:
                z =rightMostSignMinus
                
            val = val[z:]
            # if val come like '-  ' or '+   ' or '+' or '-' without value then add '1' to val
            if(val[-1] ==" " or val=="+" or  val=="-"  ):
                val = val +"1"
            
            # remove space between sign and value
            b = val
            c=""
            for i in range(len(b)):
                if(i !=0 and b[i]==" " ):
                     c = b[i+1:]
                 
                else:
                     if(c==""):
                         c = b[i+1:]
                     val = b[0]+c
                     if(i!=0):
                         break;
                
        else:
            val = "0"

        
    if (integer==True):
        val = float(val)
        val = round(val)
        return val
    
    else:
        val = float(val)
        return val
    

def find_Expression(func,integer =False):
    if(integer != True):
        if(func.find(">=") != -1):
            return ">="
        elif(func.find("<=") != -1):
            return "<="
        elif(func.find("<") != -1 and func.find("=") == -1):
            return "<"
        elif(func.find(">") != -1 and func.find("=") == -1):
            return ">"
        elif(func.find("=") != -1 and func.find(">") == -1 and func.find("<") == -1 ):
            return "="
    elif(integer == True):
        if(func.find(">=") != -1):
            return -1
        elif(func.find("<=") != -1):
            return 1
        elif(func.find("<") != -1 and func.find("=") == -1):
            return 2
        elif(func.find(">") != -1 and func.find("=") == -1):
            return -2
        elif(func.find("=") != -1 and func.find(">") == -1 and func.find("<") == -1 ):
            return 0


def find_Constant(func,integer=False):
    sign=find_Expression(func)
    signPos=func.find(sign)
    if(len(sign) ==2):
        const = func[signPos+2:]
    else:
        const = func[signPos+1:]
        
    
    
    
    if (integer==True):
        const = float(const)
        const = round(const)
        return const
    
    else:
        const = float(const)
        return const
    
    
def help():
    print("find_Xcoffiecient(variable name ,expression,integer=False)")
    print("find_Expression(expression,integer =False)")
    print("find_Constant(expression,integer=False)")
    print("")
    print("note: find_Expression integer representation")
    print(">= -1: , <= 1 : , > : -2 , < : +2 , = : 0")
    
    



    
#func ='x1 +  3.5x2 -1.56x3  >=  10.5'
#name ='x3'
#a=find_Xcoffiecient(name,func )


#print(a)

#a=find_Constant(func)
#print(a)