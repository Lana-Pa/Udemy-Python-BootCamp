class Cylinder(object):
    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def set_radius(self,new_radius):
        self.radius = new_radius
        
    def volume(self):
        return self.pi * (self.radius)**2 * self.height
         
    def surface_area(self):
        return 2 * self.pi * self.radius * self.height + 2 * self.pi * self.radius**2


height = 20
radius = 10
cyl = Cylinder(height,radius)

print 'Cylinder height is: ', cyl.height
print 'Cylinder radius is: ', cyl.radius
print 'Cylinder volume is: ', cyl.volume()
print 'Cylinder area is: ', cyl.surface_area()
