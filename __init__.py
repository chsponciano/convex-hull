""" Academic: Carlos Henrique Ponciano da Silva
    Practical work 01 [Convex Hull] 
    10078 - The Art Gallery - https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1019 """

#### Coordinate class, aids in the virtualization of points ####
class Point():
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

#### Validates program entries against problem specifications ####
def validate_input(input:list) -> list:
    _number_points = 0
    _out_points = list()
    _current_points = list()

    for element in input:
        if type(element) is tuple:
            _current_points.append(Point(element[0], element[1]))

        elif type(element) is int:
            if len(_current_points) > 0:
                if (_number_points == len(_current_points)):
                    _out_points.append(_current_points)
                    _current_points = list()
                else:
                    raise Exception('Number of invalid points!')

            if 3 > element or element > 50:
                return _out_points

            _number_points = element

#### Vector product calculation ####
def ccw(p1: Point, p2: Point, p3: Point) -> bool:
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x) < 0.000001

#### Get the guidance to go through the scenery ####
#### Returns the index of dos to the next point ####
def _get_orientation(points:list, hull_size:int, initial:int) -> int:
    _y = (initial + 1) % hull_size
    for i in range(hull_size):
        if not ccw(points[initial], points[i], points[_y]):
            _y = i
    return _y

#### Get the leftmost point ####
#### Returns the index of the leftmost point ####
def far_left(points:list) -> int:
    _idx = 0
    for i in range(1, len(points)):
        if (points[i].x < points[_idx].x) or ((points[i].x == points[_idx].x) and (points[i].y > points[_idx].y)):
            _idx = i
    return _idx

#### Convex wrapping algorithm: ####
#### 1. We obtain the leftmost point and initialize the variables. ####
#### 2. Inside the loop, we look for directions until the orientation is equal to the leftmost point. ####
#### 3. At the end we compare the size to define if there is a critical point. ####
def convex_hull(points:Point, hull_size:int) -> bool:
    _x = _far_left = far_left(points)
    _temp_hull = list()

    while(True):
        _temp_hull.append(_x)
        _x = _get_orientation(points, hull_size, _x)

        if _x == _far_left:
            break

    return len(_temp_hull) == hull_size

def is_critial_point(input:list) -> list:
    return ['No' if convex_hull(p, len(p)) else 'Yes' for p in validate_input(input)]

if __name__ == "__main__":
    _input = [4, (0,0), (3,0), (3,3), (0,3), 4, (0,0), (3,0), (1,1), (0,3), 0]
    print(is_critial_point(_input))