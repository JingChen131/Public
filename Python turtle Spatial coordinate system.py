import turtle
turtle.left(45)
#向左转45度,原默认方向向右
turtle.fd(150)
#向海龟的正前方前进150个单位
turtle.right(135)
#向右转135度
turtle.fd(300)
turtle.left(135)
turtle.fd(150)
turtle.left(45)
turtle.bk(150)
turtle.seth(45)
turtle.fd(150)
turtle.seth(60)
turtle.forward(150)
#向反方向前进150单位
#默认海龟方向向上为正方向，反之为反方向
#turtle.penup():表示抬起画笔，海龟在飞行；可以简写成turtle.pu()
#turtle.pendown():表示画笔落下，海龟在爬行；可以简写成turtle.pd()
#turttle.pensize(width):表示画笔的宽度，也可以使用turtle.width(width)
#turtle.pencolor(color):color为颜色字符串或者 RGB值；
#turtle.forward(d):向前行进距离；可以简写为turtle.fd(d)，d为整数可以为负数；
'''turtle.circle(r,extent=NONE):根据半径r绘制extent角度的弧形,
r默认在圆心左侧R距离的位置;extent:绘制角度默认360度是整圆;'''