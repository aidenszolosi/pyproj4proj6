####pyth proj testing


def lbtokg(lb):
    return float(lb) * 0.45359237


lbInput = input('\nWeight (pounds): ')
weightKG = lbtokg(lbInput)
weightKG = round(weightKG, 2)


def inchesToMeters(inches):
    return float(inches) * 0.0254 

inch = input('\nHeight (inches): ')
heightM = inchesToMeters(inch)


def bmi(weight, height):
    return weight / (height * height)

bmiNumber = bmi(weightKG, heightM)
bmiNumber = round(bmiNumber, 1)
bmiNumber = str(bmiNumber)
print('BMI INDEX VALUE IS: ' + bmiNumber)

#this fixes it not recognizing numbers without .0
bmiNumber = str(float(bmiNumber))

#create table of possible values
xlist = []

for x in range(18, 26):
    x = round(x, 1)
    xlist.insert(0, str(x) + str('.1'))
    xlist.insert(1, str(x) + str('.2'))
    xlist.insert(2, str(x) + str('.3'))
    xlist.insert(3, str(x) + str('.4'))
    xlist.insert(4, str(x) + str('.5'))
    xlist.insert(5, str(x) + str('.6'))
    xlist.insert(6, str(x) + str('.7'))
    xlist.insert(7, str(x) + str('.8'))
    xlist.insert(8, str(x) + str('.9'))
    xlist.insert(0, str(x) + str('.0'))
    if bmiNumber in xlist: 
        bmiNormal = True

    if bmiNumber not in xlist:
        bmiNormal = False
if float(bmiNumber) <= float(18.5):
    bmiUnderweight = True
else:
    bmiUnderweight = False


if float(bmiNumber) >= float(30):
    bmiObese = True
else:
    bmiObese = False

##
ylist = []


#BUG: Solved
for y in range(25, 30):
    ylist.insert(0, str(y) + str('.0'))
    ylist.insert(1, str(y) + str('.1'))
    ylist.insert(2, str(y) + str('.2'))
    ylist.insert(3, str(y) + str('.3'))
    ylist.insert(4, str(y) + str('.4'))
    ylist.insert(5, str(y) + str('.5'))
    ylist.insert(6, str(y) + str('.6'))
    ylist.insert(7, str(y) + str('.7'))
    ylist.insert(8, str(y) + str('.8'))
    ylist.insert(9, str(y) + str('.9'))
if bmiNumber in ylist: 
        bmiOverweight = True

if bmiNumber not in ylist:
        bmiOverweight = False


if bmiUnderweight:
    print('BMI value indicates underweight')
elif bmiNormal:
    print('BMI is normal')
elif bmiOverweight:
    print('BMI indicates overweight')
elif bmiObese:
    print('BMI value indicates obesity')
