# LinearProgramming

Hello World!.. This is kisal Rojitha Thenuwara

I have created a LP slover using simplex method which I learned from my university studies.

currently it's working only for maximization problems and all constraints must be less than or equal type.like below.

ex:  2x1 + 3x2 + 4x3 <=  100

its working for any number of variables.

I will fix it for other type of constraints and  for also minimization problems.

modules you may need to install to run this:

	: tabulate
	: numpy('probably built-in')


first you have to open the Krt_lp folder and inside it you will find a python file called KisalLpSolver.
open that file and only thing you need to do is edit the string inside of that file as to solve your lp problem


a = """

        Max z = 40x1 + 30x2 

            x1 + x2   <= 12 ,
    
            2x1 + x2  <= 16 
    
                         
                          
"""

note : put a comma  end of each constraint except last one
	   when writing objective function leave spaces each side of the '+' , '-' , '=' signs


Have Fun......
feel free to use and edit this code as yours.........











