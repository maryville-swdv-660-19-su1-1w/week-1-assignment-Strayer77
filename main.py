#uses random_name to generate a list of random names
#and then uses pygal to create a bar graph that charts
#the names based on number of characters in each name
#and renders to browser window
import random_name
import pygal


#uses random_name to generate a list of 5 random names
def getFakeNames():
        names = random_name.generate(5)
        return names



#takes the list of names and gets a letter count
#for each name and adds it to it's own list
def countLettersInNames(namesList):
    letterCountList = []
    for name in namesList:
        name = name.replace(" ", "")
        letterCount = len(name)
        letterCountList.append(letterCount)

    return(letterCountList)

        

def main():

    namesList = getFakeNames()
    letterCount = countLettersInNames(namesList)

    print(namesList, letterCount)

    bar_chart = pygal.Bar()
    bar_chart.add('Names', letterCount)
    bar_chart.x_labels = namesList
    bar_chart.render_in_browser()
    print("Chart is being created")

    input("Press enter to continue.")
    
main()




