#helloWorld.py
#This is my first python script after DevNet courses
print('Hello World')
print()
fruits={'Apples':['Granny Smith','Red Delicious','Green'],'Peaches':['Red Haven','Sun Crest'],'Berries':['Strawberries','Blue Berries','Black Berries']}
print("Select your favorite Fruit: \n",end=' ')
for i in fruits:
    print(i+',',end=' ')

userInput=input(': ')
print("\n")
print("You should try: \n\n",end=' ')
for e in fruits[userInput]:
    print(e,end=' ')
    print(userInput)
    print()