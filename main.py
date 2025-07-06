from graphics import *
from DiceGraphics import layout
import random

def buttons(win, x1, y1, x2, y2, label):
    rect = Rectangle(Point(x1,y1), Point(x2,y2))
    rect.setFill("darkgrey")
    rect.draw(win)
    text = Text(Point((x1+x2)/2, (y1+y2)/2), label)
    text.draw(win)
    return (x1,y1,x2,y2)
    
def is_clicked(pt, bounds):
    x, y = pt.getX(), pt.getY()
    x1, y1, x2, y2 = bounds
    return x1<=x<=x2 and y1<=y<=y2

def main():
    win = GraphWin("Dice Roller Game", 400, 400)
    win.setBackground("lightblue")
    
    layout(win, 1, offset=0)
    layout(win, 1, offset=150)
    
    result = Text(Point(200, 180), "Numbers rolled : (1,1)")
    result.setSize(18)
    result.setStyle("bold")
    result.setTextColor("darkgreen")
    result.draw(win)
    
    rollBtn = buttons(win, 50, 250, 150, 300, "Roll")
    quitBtn = buttons(win, 250, 250, 350, 300, "Quit")
    
    while True:
        pt = win.getMouse()
        if is_clicked(pt, quitBtn):
            break
        elif is_clicked(pt, rollBtn):
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            layout(win, d1, offset=0)
            layout(win, d2, offset=150)
            result.setText(f"Numbers rolled : ({d1},{d2})")
    win.close()
    
main()

