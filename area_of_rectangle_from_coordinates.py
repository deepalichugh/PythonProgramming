# You are given a rectangle in a plane. 
# The coordinates of one of its diagonals are provided to you. 
# You have to print the total area of the rectangle.
# The coordinates of the rectangle are provided as four integral values: x1, y1, x2, y2. It is given that x1 < x2 and y1 < y2.


def area_of_rectange(x1, y1, x2, y2):
    height = y2 - y1
    length = x2 - x1

    area = (height*length)
    return area

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(area_of_rectange(x1, y1, x2, y2))