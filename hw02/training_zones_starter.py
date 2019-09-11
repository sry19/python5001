def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    #compute the maximum heart rate and reserve
    max_heart_rate = 208 - 0.7 * age
    reserve=max_heart_rate-restHR
    print("Your heart rate reserve is:",reserve,"bpm")
    print("Here is a breakdown of your training zones:")

    #difine low bound and high bound constants
    #difine distance between low bound and previous high bound
    ZONE1_LB=0.5
    ZONE2_LB=0.6
    ZONE3_LB=0.7
    ZONE4_LB=0.8
    ZONE5_LB=0.93
    ZONE5_HB=1
    LB_TO_HB=0.01

    #compute zone1
    zone1_low=restHR+reserve*ZONE1_LB
    zone1_high=restHR+reserve*ZONE2_LB
    print("Zone 1:",round(zone1_low,2),"to",round(zone1_high,2),"bpm")

    #compute zone2
    zone2_low=restHR+reserve*ZONE2_LB+LB_TO_HB
    zone2_high=restHR+reserve*ZONE3_LB
    print("Zone 2:",round(zone2_low,2),"to",round(zone2_high,2),"bpm")

    #compute zone3
    zone3_low=restHR+reserve*ZONE3_LB+LB_TO_HB
    zone3_high=restHR+reserve*ZONE4_LB
    print("Zone 3:",round(zone3_low,2),"to",round(zone3_high,2),"bpm")

    #compute zone4
    zone4_low=restHR+reserve*ZONE4_LB+LB_TO_HB
    zone4_high=restHR+reserve*ZONE5_LB
    print("Zone 4:",round(zone4_low,2),"to",round(zone4_high,2),"bpm")

    #compute zone5
    zone5_low=restHR+reserve*ZONE5_LB+LB_TO_HB
    zone5_high=restHR+reserve*ZONE5_HB
    print("Zone 5:",round(zone5_low,2),"to",round(zone5_high,2),"bpm")

    print("=======================================")

main()