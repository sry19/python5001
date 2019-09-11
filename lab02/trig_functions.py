import math

def main():
    #input angle
    angle=float(input("Enter an angle: "))

    #compute cosine and sine
    cosine=math.cos(math.radians(angle))
    sine=math.sin(math.radians(angle))
    
    #print cosine and sine
    print("The cosine of",angle,"is",cosine)
    print("The sine of",angle,"is",sine)

    
main()