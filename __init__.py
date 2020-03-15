import time


class Coordinate:
    def __init__(self, x, y):
        self._x = x
        self._y = y

def _leftmost(coordinates:list) -> int:
    _index = 0
    for i in range(1, len(coordinates)):
        if (coordinates[i]._x < coordinates[_index]._x) or ((coordinates[i]._x == coordinates[_index]._x) and (coordinates[i]._y > coordinates[_index]._y)):
            _index = i
    return _index

def _get_orientation(p:Coordinate, q:Coordinate, r:Coordinate) -> int:
    _v = ((q._y - p._y) * (r._x - q._x)) - ((q._x - p._x) * (r._y - q._y))
    
    if _v == 0:
        return 0
    elif _v > 0:
        return 1
    else:
        return 2

def _convex_hull(coordinates:list) -> list:
    _lm = _leftmost(coordinates)
    _n = len(coordinates)
    _hull = list()
    _x = _lm

    while(True):
        _hull.append(_x)
        _y = (_x + 1) % _n
        for i in range(_n):
            if _get_orientation(coordinates[_x], coordinates[i], coordinates[_y]) == 2:
                _y = i
        _x = _y
        if _x == _lm:
            break
    
    return [(coordinates[p]._x, coordinates[p]._y) for p in _hull]

def isCriticalPoint(inputs:list) -> str:
    _number_points = 0
    _output = list()
    _current_points = list()

    for element in inputs:
        if type(element) is tuple:
            _current_points.append(Coordinate(element[0], element[1]))

        elif type(element) is int:
            if len(_current_points) > 0:
                _convex = _convex_hull(_current_points)
                _output.append('No' if len(_convex) == len(_current_points) else 'Yes')
                _current_points = list()

            if 3 > element or element > 50:
                return _output

            _number_points = element
    
if __name__ == "__main__":
    _input = [4, (0,0), (3,0), (3,3), (0,3), 4, (0,0), (3,0), (1,1), (0,3), 0]

    _start_time = time.time()
    print(isCriticalPoint(_input))
    print(f'Runtime: {time.time() - _start_time}')