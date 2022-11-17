####pyth proj testing

print('-' * 50)
print('Inputs:')
def lbtokg(lb):
    return float(lb) * 0.45359237


lbInput = input('  Weight (pounds): ')
weightKG = lbtokg(lbInput)
weightKG = round(weightKG, 2)


def inchesToMeters(inches):
    return float(inches) * 0.0254 

inch = input('  Height (inches): ')
heightM = inchesToMeters(inch)

ageIn = input('  Current age (years): ')
try:
    ageIn = int(ageIn)
except ValueError: 
    print('This was not a valid integer value.')
    exit() 

rhrIn = input('  Resting heart rate (BPM): ')
try:
    rhrIn = int(rhrIn)
except ValueError: 
    print('This was not a valid integer value.')
    exit() 


def bmi(weight, height):
    return weight / (height * height)

bmiNumber = bmi(weightKG, heightM)
bmiNumber = round(bmiNumber, 1)
bmiNumber = str(bmiNumber)
print('-' * 50)
print('BMI VALUE: ' + bmiNumber)

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
    print('BMI value indicates the patient is within the underweight range')
elif bmiNormal:
    print('BMI value indicates the patient is within the normal range')
elif bmiOverweight:
    print('BMI value indicates the patient is within the overweight range')
elif bmiObese:
    print('BMI value indicates the patient is within the obesity range')


##BMI CALCULATIONS ARE DONE, NOW FOR KARVONEN FORMULA

def karFormula(age, rhr, maxHeartVal):
    ###maximum heart rate
    mhr = 220 - int(age)
    #print(mhr)
    ###heart rate reserve
    hrr = int(mhr) - int(rhr)
    #print(hrr)
    ###maximum target zone
    mtz = int(hrr)*float(maxHeartVal)
    #print('mtz is' + str(mtz))
    lastval = float(mtz) + float(rhr)
    #print(lastval)
    return lastval
    #target training zone
    ##ttz = mtz + rhr



print('Exercise Intensity Heart Rates: ')
print('Intensity(%)' + '\tMax Heart Rate(BPM)')
#Create allowed values for maximum intensity
for i in range(50, 96, 5):
    #print(str(maxHeartVal) + '%')
    #output = karFormula(age, maxHeartVal)
    #print(output)
    i = float(i)
    i = i / 100
    result = karFormula(ageIn,rhrIn,i)
    result = int(result)
    print((str(int(i * 100)) + '%') + '\t\t' + str(result))
   
