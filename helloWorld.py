#helloWorld.py
#This is my first python script after DevNet courses
print('Hello World')
print()
fruits={'Apples':['Granny Smith','Red Delicious','Green'],'Peaches':['Red Haven','Sun Crest'],'Berries':['Strawberries','Blue Berries','Black Berries']}
def myFavouriteFruitFinder():
    print("Select your favorite Fruit\n",end=' ')
    for i in fruits:
        print(i) 
myFavouriteFruitFinder()