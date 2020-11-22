height=int(input('Enter the initial height: '))
times=int(input('Enter the number of times the ball is allowed to continue to bounce: '))

distance=height
speed=distance
for i in range(times):
    height=height*2
    if i+1==times:
        distance+height/9.8
    else:
        distance=distance+height /9.8
            
print('\nTotal speed of travel by the ball is', )
