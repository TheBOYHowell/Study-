import random

question=input('Question : ')
i = random.randint(1, 9)
if i==0:
    answer=('Yes - definitely.')
elif i==1:
    answer=('It is decidedly so.')
elif i==2:
    answer=('Without a doubt.')
elif i==3:
    answer=('Reply hazy, try again.')
elif i==4:
    answer=('Ask again later.')
elif i==5:
    answer=('Better not tell you now.')
elif i==6:
    answer=('My sources say no.')
elif i==7:
    answer=('Outlook not so good.')
elif i==8:
    answer=('My sources say no.') 
elif i==9:
    answer=('Very doubtful.')
print(answer)