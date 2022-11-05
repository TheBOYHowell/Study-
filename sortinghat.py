Gry=0;Rav=0;Huf=0;Sly=0          #  🦁  Gryffindor 🦅 Ravenclaw 🦡 Hufflepuff 🐍 Slytherin

print("Q1) Do you like Dawn or Dusk?" )
print("1) Dawn " )
print("2) Dusk " )
AQ1=int(input("Choice your answer : "))                     #AQ1 = Answer Question 1 
if AQ1==1 :
    Gry=Gry+1
    Rav=Rav+1
elif AQ1==2:
    Huf=Huf+1
    Sly=Sly+1
else :
    while not(AQ1 in range (1,3)) :
     print("Wrong input ")
     AQ1=int(input("Choice your answer : "))
print("Q2) When I’m dead, I want people to remember me as:" )
print("1) The Good ")
print("2) The Great ")
print("3) The Wise ")
print("4) The Bold ")
AQ2=int(input("Choice your answer : "))                    #AQ2 = Answer Question 2
if AQ2==1:
    Huf=Huf+1
elif AQ2==2:
    Sly=Sly+1
elif AQ2==3:
    Rav=Rav+1
elif AQ2==4:
    Gry=Gry+1
else:
    while not(AQ2 in range (1,5)) :
     print("Wrong input ")
     AQ2=int(input("Choice your answer : "))
print("Q3) Which kind of instrument most pleases your ear?" )
print("1) The violin ")
print("2) The trumpet ")
print("3) The piano ")
print("4) The drum ")
AQ3=int(input("Choice your answer : "))                     #AQ3 = Answer Question 3 
if AQ3==1:
    Sly=Sly+1
elif AQ3==2:
    Huf=Huf+1
elif AQ3==3:
    Rav=Rav+1
elif AQ3==4:
    Gry=Gry+1
else:
    while not(AQ3 in range (1,5)) :
     print("Wrong input ")
     AQ3=int(input("Choice your answer : "))
print("Your house is : ")
if Gry >= Rav and Gry >= Huf and Gry >= Sly:
  print('🦁 Gryffindor!')
elif Rav >= Huf and Rav >= Sly:
  print('🦅 Ravenclaw!')
elif Huf >= Sly:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
