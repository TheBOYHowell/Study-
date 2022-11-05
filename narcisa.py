def narcissistic( value ):
        a=0
        x=str(value)
        v=len(x)
        for i in range (0,v):
            a= int(x[i])**v+a
        if value==a :
            return 1
        else :
            return 0

