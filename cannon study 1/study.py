from graphics import *




win = GraphWin("hello",300,300)
gun = Polygon(Point(120,280), Point(180,280), Point(150,250))
gun.draw(win)
while 1:
    x = win.getMouse()
    point_x = x.getX()
    point_y = x.getY()
    if point_y > 280:
        break
    c = Circle(Point(150,250),5)
    c.draw(win)
    circle_x = c.getCenter().x
    circle_y = c.getCenter().y
    gap_x = circle_x - point_x
    gap_y = circle_y - point_y
    move_x = 1*gap_x/gap_y
    while c.getCenter().y > point_y:
        c.move(-move_x,-1)
    c.undraw()




win.close()