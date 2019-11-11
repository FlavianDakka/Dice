# math_gui.py
# Interactive GUI for simple math involving two variables.

from graphics import *

def main():
    
    win = GraphWin(title="Dice Roller", width=300, height=240)
    
    win.setBackground(color_rgb(204,236,255))
    
    xtext = Text(Point(20,30), "D2")
    xtext.setSize(10)
    xtext.draw(win)
    ytext = Text(Point(20, 60), "D4")
    ytext.setSize(10)
    ytext.draw(win)
    ftext = Text(Point(20,90), "D6")
    ftext.setSize(10)
    ftext.draw(win)
    atext = Text(Point(100,30), "D8")
    atext.setSize(10)
    atext.draw(win)
    btext = Text(Point(100,60), "D10")
    btext.setSize(10)
    btext.draw(win)
    ctext = Text(Point(100,90), "D12")
    ctext.setSize(10)
    ctext.draw(win)
    
    outputtext = Text(Point(150,140), "x + y = 3")
    outputtext.setSize(18)
    outputtext.setStyle("italic")
    outputtext.setTextColor("red")
    outputtext.draw(win)
    
    
    
    
    xentry = Entry(Point(60,30), 5)
    xentry.setFill("white")
    xentry.setText("0")
    xentry.draw(win)
    
    yentry = Entry(Point(60,60), 5)
    yentry.setFill("white")
    yentry.setText("0")
    yentry.draw(win)

    fentry = Entry(Point(60,90), 5)
    fentry.setFill("white")
    fentry.setText("0")
    fentry.draw(win)
    
    aentry = Entry(Point(140,30), 5)
    aentry.setFill("white")
    aentry.setText("0")
    aentry.draw(win)
    bentry = Entry(Point(140,60), 5)
    bentry.setFill("white")
    bentry.setText("0")
    bentry.draw(win)
    centry = Entry(Point(140,90), 5)
    centry.setFill("white")
    centry.setText("0")
    centry.draw(win)
    # Add button object
    
    rect = Rectangle(Point(100, 170), Point(200, 210))
    rect.setFill("cyan")
    rect.draw(win)
    txt = Text(Point(150, 190), 15)
    txt.setText("OK")
    txt.draw(win)
    #***Add/modify code here**
    pt = win.getMouse()
    # As long as the window is open, allow multiple computations
    while True:
        # Wait for user input
        #***Add/modify code here**
        
        # Extract inputs
        #***Add/modify code here**
        x = float(xentry.getText())
        y = float(yentry.getText())
        f = fentry.getText()
        
        # Evaluate the function using the two inputs
        z = eval(f)
        
        # Update the output text
        #***Add/modify code here**
        a = str(f)
        b = (a, '=', z)
        outputtext.setText(b)


main()
