#inv = ["a", "b", "c"]

#for c in inv:
#    print(c)
#

bmiNumber = input()
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

if bmiNormal:
    print('BMI is normal')
else: 
    print('BMI is not normal')


#if bmiNumber < 18.5:
    #print('The index value has indicated the patient is underweight.')
    
#elif bmiNumber == range(18.5, 24.9):
    #print
