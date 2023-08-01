from Card import Card
from Deck import Deck


    
'''
Note: DO NOT MODIFY THIS FUNCTION. If your grid is not displaying properly, check your code first or contact us. 

displays a grid of cards arranged in 7x5 col/row formatted like this:
[   [row1, row2, row3...],  <-col1
    [row1, row2, row3...],  <-col2
    [row1, row2, row3...],  <-col3
    ...
]

params:
    grid - a 2D list in the format shown above

returns:
    None (output from this function is printed)

'''
def displayGrid(grid):

    #generate and display the index header for the grid
    headerStr = ""
    for row in range(7):
        headerStr += " \t" + str(row) + "\t "
    print(headerStr)
    print()

    #proces through each of the rows in reverse because we need to print top to bottom (ie last index to first)
    for row in range(4, -1, -1):

        #generate the full string for a row before printing it
        rowStr = "|\t"
        for col in range(7):
            #create an index offset so that cards are always aligned at the top
            offset = 5 - len(grid[col])
            rowIdx = row - offset

            #as long as the row index is valid, get the data for that particular card
            if(rowIdx >=0):
                rowStr += str(grid[col][rowIdx]) + "\t|\t"
            
            #otherwise print an empty space
            else:
                rowStr += "  \t|\t"
            
        #print the completed row and a row separator
        print(rowStr)
        print()

#---------------------------------------------------------------------------------------------------------------

#Initializes a grid of cards for golf solitaire

def initGrid(deck):
    arr=[]
    for i in range(7):
        col = []
        for j in range(5):
            col.append(deck.drawCard())
        arr.append(col)

    # returns a 2D list of card objects formatted in a 7x5 configuration for 7 columns and 5 rows
    return arr




#Checks whether the grid is empty (ie the grid is a list containing only empty lists)

def checkWin(grid):

    #returns:
    #True if the grid is empty
    #False if the grid is not empty

    for i in grid:
        if i!=[]:
            return False
    return True


    
#calculates the abs between the values of two cards

def compareCards(card1, card2):
    card1 = card1.getValue()
    card2 = card2.getValue()

    #returns the absolute value between the two cards (not accounting for A and K)
    return abs(card2-card1)


def main():
    deck = Deck()
    grid = initGrid(deck)
    displayGrid(grid)

    #creating a new list to store the waste pile
    wastePile=[]
    print ("Waste pile: None")

    #runs the game only when the grid is NOT empty

    while checkWin(grid)==False:

        #asks the user for input
        userInput=input("Enter an index to remove or 'd' to select a card from the deck. Enter 'q' to quit.")
        
       
        #uses 3 main conditionals on the outside to check if user input "index", "d" or "q"
        if userInput == "d":
            #cardsleft=Deck.cardsLeft()
            #if cardsleft!=0:
            if deck != 0:
                drawnCard= deck.drawCard()

                #appends the card drawn from the deck to the waste pile
                wastePile.append(drawnCard)
                displayGrid(grid)
                print("Waste Pile:" ,drawnCard)
            else:
                  
               #ends the game when there are no more cards left in the deck
               print("You have lost the game. There are no more cards left in the deck. Please try again. ")
               quit()
           
        
        #ends the game when user chooses "q"
        elif userInput=="q":
            
            print("You have successfully quitted the game")
            quit()

        
        else:
            u = int(userInput)

            #checks if the index is within the range
            if u>=0 and u<=6:

                #removes the card from the grid by using the index given by the user
                cardRemoved=grid[u][0]
                grid[u].pop(0)
            
                # allows the user to draw any card from the grid when the waste pile is empty
                if wastePile==[]:
                    wastePile.append(cardRemoved)
                    displayGrid(grid)
                    print ("Waste Pile:", cardRemoved)


                #allows the user to draw a card only when the difference between topmost card in wastepile and cadremoved is |1|
                else:
                    absvalue=compareCards(wastePile[len(wastePile)-1],cardRemoved)
                    if absvalue==1:
                        wastePile.append(cardRemoved)
                        displayGrid(grid)
                        print("Waste Pile:",cardRemoved)

                #displays an error message if a user chooses a card against the game rules   
                    else:
                        print("You cannot draw this card. Please choose again")
        
    print("Congratulations! You have won the game.") 

            
if __name__ == "__main__":
    main()









