def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    #TODO: Fill in the rest of the necessary code here
    max_heart_rate = 208 - 0.7 * age
    reserve=max_heart_rate-restHR
    print("Your heart rate reserve is:",reserve,"bpm")
    print("Here is a breakdown of your training zones:")
    zone1low=restHR+reserve*0.5
    zone1high=restHR+reserve*0.6
    print("Zone 1:",round(zone1low,2),"to",round(zone1high,2),"bpm")
    zone2low=restHR+reserve*0.6+0.01
    zone2high=restHR+reserve*0.7
    print("Zone 2:",round(zone2low,2),"to",round(zone2high,2),"bpm")
    zone3low=restHR+reserve*0.7+0.01
    zone3high=restHR+reserve*0.8
    print("Zone 3:",round(zone3low,2),"to",round(zone3high,2),"bpm")
    zone4low=restHR+reserve*0.8+0.01
    zone4high=restHR+reserve*0.93
    print("Zone 4:",round(zone4low,2),"to",round(zone4high,2),"bpm")
    zone5low=restHR+reserve*0.93+0.01
    zone5high=restHR+reserve
    print("Zone 5:",round(zone5low,2),"to",round(zone5high,2),"bpm")
    print("=======================================")

main()