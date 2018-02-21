from math import sqrt

class Line(object):

    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return sqrt(((self.coor2[0]-self.coor1[0])**2) + ((self.coor2[1]-self.coor1[1])**2))

    def slope(self):
        return (self.coor2[1] - self.coor1[1])//(self.coor2[0]-self.coor1[0])


coordinate1 = (2,3)
coordinate2 = (3,4)

a = Line(coordinate1,coordinate2)

print 'Coordinate 1 = ', a.coor1
print 'Coordinate 2 = ', a.coor2

print 'The distance is: ', a.distance()
print 'The slope is: ', a.slope()

