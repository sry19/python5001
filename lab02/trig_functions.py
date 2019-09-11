import math

def main():
    angle=float(input("Enter an angle: "))
    cosine=math.cos(math.radians(angle))
    sine=math.sin(math.radians(angle))
    print("The cosine of",angle,"is",cosine)
    print("The sine of",angle,"is",sine)

    
main()