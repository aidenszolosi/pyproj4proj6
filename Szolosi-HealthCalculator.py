#Programmer - Aiden Szolosi
#Date - 11/17/22
#Name - Szolosi-HealthCalculator.py
#Description:
    #The purpose of this assignment is to create a health calculator. The health calculator
    #is to calculate a BMI value and analyze what it means. The calculator must also
    #calculate the maximum heart rate per intensity level. 
    #The range we will calculate in this calculator is 50%-95%. 
    #The calculator accepts the following inputs:
        #Weight                 (lb)
        #Height                 (in)
        #Age                    (yr)
        #Resting Heart Rate     (bpm)
    #The calculator should return the following outputs:
        #BMI Value
        #BMI Value analysis
        #Intensity Percentages between 50-95
        #Max Heart Rate corresponding with intensity % based on Karvonen formula
    #The calculator will also format the output to make the program's response easy to read 

#Learning Objectives (## means checked off):
    ##Input data from user 
    ##Perform several different calculations
    ##Process data within a loop
    ##Make output choices based on conditional logic
    ##Output information to user
    ##Read string input from the console and convert input to required numeric data-types
    ##Convert math formulas to Python code
    ##Research and apply correct conversion formulas
    ##Understand the if / elif / else construct
    ##Output numeric data to specific decimal places
#I apologize for the messy code.
#--------------------------------------------------------------------------------------------#

print('-' * 50)
print('Inputs:')
def lbtokg(lb):
    return float(lb) * 0.45359237

def inchesToMeters(inches):
    return float(inches) * 0.0254 

inch = input('  Height (inches): ')
heightM = inchesToMeters(inch)


lbInput = input('  Weight (pounds): ')
weightKG = lbtokg(lbInput)
weightKG = round(weightKG, 2)




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
bmiNumber = round(bmiNumber, 2)
bmiNumber = str(bmiNumber)
print('-' * 50)
print('Results:')
print(' BMI VALUE: ' + bmiNumber)

#this fixes it not recognizing numbers without .0
bmiNumber = round(float(bmiNumber), 1)
bmiNumber = str(float(bmiNumber))
#create table of possible values
xlist = []

for x in range(18, 25):
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

bmiNumber = float(bmiNumber)
bmiNumber = round(bmiNumber, 1)


if float(bmiNumber) <= float(18.5):
    bmiUnderweight = True
else:
    bmiUnderweight = False


if float(bmiNumber) >= float(30):
    bmiObese = True
else:
    bmiObese = False

##

bmiNumber = round(float(bmiNumber), 1)
bmiNumber = str(float(bmiNumber))
ylist = []



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
    print(' BMI Range: UNDERWEIGHT')
elif bmiNormal:
    print(' BMI Range: NORMAL')
elif bmiOverweight:
    print(' BMI Range: OVERWEIGHT')
elif bmiObese:
    print(' BMI Range: OBESE')


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


print('' * 10 + '-' * 25)
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
    print(' ' + (str(int(i * 100)) + '%') + '\t\t' + str(result))
print('-' * 50)
