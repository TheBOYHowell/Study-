def narcissistic( value ):
        a=0
        x=str(value)
        v=len(x)
        for i in range (0,v):
            a= int(x[i])**v+a
        if value ==a :
            return True
        else : return False
    #https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python