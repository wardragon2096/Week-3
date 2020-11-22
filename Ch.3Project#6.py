iterations=int(input('Enter the number of iterations: ')) 
value=1 
c=3 
if iterations==1: 
    value=1 
else:
    for i in range(iterations-1): 
        value=value+(1/c)*((-1)**(i+1)) 
        c=c+2
        
print('The approximate value of pi is:',value) 
