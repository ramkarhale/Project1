

class Point:
     def __init__(self, x=0, y=0): #Constructor
        self.x = x
        self.y = y

     def show_points(self):
         print("x coordinate is",self.x)
         print("y coordinate is",self.y)

class Line(Point):
    def __init__(self, startPoint, endPointy):
        Point.__init__(self)
        self.startPoint = startPoint
        self.endPoint = endPointy





if __name__=="__main__":
    p1 = Point(10,20) 
    p2 = Point(30,40)

    l=Line(p1,p2)
    l.showLine()

    p1.show_points()      


