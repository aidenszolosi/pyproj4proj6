####pyth proj testing


def lbtokg(lb):
    return float(lb) * 0.45359237


lbInput = input('\nWeight (pounds): ')
weightKG = lbtokg(lbInput)
weightKG = round(weightKG, 2)
print(weightKG)

def inchesToMeters(inches):
    return float(inches) * 0.0254 

inch = input('\nHeight (inches): ')
heightM = inchesToMeters(inch)
print(heightM)

def bmi(weight, height):
    return weight / (height * height)

bmiNumber = bmi(weightKG, heightM)
bmiNumber = round(bmiNumber, 1)
bmiNumber = str(bmiNumber)
print('BMI INDEX VALUE IS: ' + bmiNumber)


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
    xlist.insert(0,str(x))
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

for y in range(25, 30):
    y = round(x, 1)
    ylist.insert(0, str(x) + str('.1'))
    ylist.insert(1, str(x) + str('.2'))
    ylist.insert(2, str(x) + str('.3'))
    ylist.insert(3, str(x) + str('.4'))
    ylist.insert(4, str(x) + str('.5'))
    ylist.insert(5, str(x) + str('.6'))
    ylist.insert(6, str(x) + str('.7'))
    ylist.insert(7, str(x) + str('.8'))
    ylist.insert(8, str(x) + str('.9'))
    ylist.insert(0,str(x))
    if bmiNumber in ylist: 
        bmiOverweight = True

    if bmiNumber not in ylist:
        bmiOverweight = False

if bmiUnderweight:
    print('BMI value indicates underweight')

if bmiNormal:
    print('BMI is normal')

if bmiOverweight:
    print('BMI indicates overweight')

if bmiObese:
    print('BMI value indicates overweight')
