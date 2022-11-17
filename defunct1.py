#PythonProject4 Lab6 

height = input('\nHeight (inches): ')
weight = input('\nWeight (pounds): ')
age = input('\nAge (Years): ')
restingHeartRate = input('\nResting Heart Rate (BPM): ') 

print('BMI INDEX')
bmivalues = [height, weight, age, restingHeartRate]
for i in bmivalues: 
    print(i)


def bmi():
    weightKG = float(weight) * 0.45359237
    unsquaredHeightInMeters = float(height) * 0.0254 
    heightM = unsquaredHeightInMeters * unsquaredHeightInMeters
    return bmi

print(bmi)
