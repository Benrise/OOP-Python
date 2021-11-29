from math import sqrt

class Point:
    list_points = []
    
    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y) 
        Point.list_points.append(self)
        
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
    def go_home(self):
        self.move_to(0,0)
        
    def print_point(self):
        print(f'Точка с координатами ({self.x}, {self.y})')
        
    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент должен принадлежать классу Point')
            
        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)