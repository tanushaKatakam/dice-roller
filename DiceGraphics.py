from graphics import *
def dots(win, x, y):
    dot = Circle(Point(x,y), 5)
    dot.setFill('black')
    dot.draw(win)
    
def layout(win, num, offset=0):
    rect = Rectangle(Point(offset+50,50), Point(offset+150,150))
    rect.setFill('white')
    rect.draw(win)
    
    dotPosition = {
        1:[(100,100)], 2:[(70,70), (130,130)], 
        3:[(70,70), (100,100), (130,130)],
        4:[(70,70), (130,70), (70,130), (130,130)], 
        5:[(70,70), (130,70), (100,100), (70,130), (130,130)],
        6:[(70,70), (130,70), (70,100), (130,100), (70, 130), (130,130)],
    }

    for x,y in dotPosition[num]:
        dots(win, x+offset, y)
    
