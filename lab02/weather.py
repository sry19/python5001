highest_temp=[73,77,71,67,62,65,63,65,67,69]
lowest_temp=[58,60,60,57,53,54,55,55,55,56]
def diff_of_temp(highest_temp,lowest_temp):
    max_high_temp=highest_temp[0]
    for i in highest_temp:
        if i>max_high_temp:
            max_high_temp=i

    min_low_temp=lowest_temp[0]
    for i in lowest_temp:
        if i <min_low_temp:
            min_low_temp=i

    difference_high_low=max_high_temp-min_low_temp
    print("The difference between the highest and the lowest temprature values predicted for the 10 day forecast:",difference_high_low,"Fahrenheit")

noon_temp=[66,69,66,64,60,60,59,60,62,63]
def ave_noon_temp(noon_temp):
    sum_temp=0
    for i in noon_temp:
        sum_temp+=i
    ave_temp=sum_temp/10
    print("The average temperature at noon predicted for the 10 day forecast is:",ave_temp,"Fahrenheit")

def convert_temp(highest_temp):
    max_high_temp=highest_temp[0]
    for i in highest_temp:
        if i>max_high_temp:
            max_high_temp=i
    c_temp=(max_high_temp-32)/1.8
    print("The highest temperature predicted for the 10 day forecast is",max_high_temp,"Fahrenheit")
    print("It is converted to",c_temp,"Celsius")


diff_of_temp(highest_temp,lowest_temp)
ave_noon_temp(noon_temp)
convert_temp(highest_temp)