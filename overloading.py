class square:
    print("print square")

    def __init__(self, side):
         self.side = side
         print("print side",side)
    
    def __add__(squareone, squaretwo): # explixitly we are overloading a add operator here 
        return((4*squareone.side) + (4*squaretwo.side))






squareone = square(5) 
squaretwo= square(10)
print("added both squares", squareone + squaretwo)