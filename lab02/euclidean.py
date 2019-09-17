import math

def main():
    # input the x and y values
    x1 = float(input("Please input x1: "))
    y1 = float(input("Please input y1: "))
    x2 = float(input("Please input x2: "))
    y2 = float(input("Please input y2: "))

    # compute the euclidean distance
    euclidean_dist = math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
    print("The distance between two 2-dimensional points is:", euclidean_dist)


main()