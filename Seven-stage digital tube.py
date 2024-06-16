import turtle as t
def drawLine(draw):
    t.pendown() if draw else t.penup()
    t.fd(40)
    t.right(90)
def drawDigit(digit):
    drawDigit(True) if digit in [2,3,4,5,6,8,9] else drawDigit(False)
    drawDigit(True) if digit in [0,1,3,5,6,8,9] else drawDigit(False)
    drawDigit(True) if digit in [0,2,3,5,6,8,9] else drawDigit(False)
    drawDigit(True) if digit in [0,2,6,8] else drawDigit(False)
    t.left(90)
    drawDigit(True) if digit in [0,4,5,6,8,9] else drawDigit(False)
    drawDigit(True) if digit in [0,2,3,5,6,7,8,9] else drawDigit(False)
    drawDigit(True) if digit in [0,1,2,3,4,7,8,9] else drawDigit(False)
    t.left(180)