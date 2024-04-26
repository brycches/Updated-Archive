

def function (x,y):
    if x ==0:
        return y
    else:
        return 1 + function(x-1,y)
    
    
print(function(5,10))