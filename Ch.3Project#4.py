height=int(input('Enter the initial height: '))
times=int(input('Enter the number of times the ball is allowed to continue to bounce: '))

distance=height
for i in range(times):
    height=height*0.6
    if i+1==times:
        distance+height
    else:
        distance=distance+(2*height)
            
print('\nTotal distance traveled by the ball is', distance)
