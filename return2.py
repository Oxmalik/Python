iterations = int(input())
num1 = int(input())
num2 = int(input())

def bigger(arg1, arg2):
    if arg1>arg2:
        print('bval: ',arg1)
        return arg1
    elif arg2>arg1:
        print('bval: ',arg2)
        return arg2
    elif arg2 == arg1:
        print('bSameval: ',arg2)
        return arg2

def smaller(arg1, arg2):
    if arg1>arg2:
        print('sval: ',arg2)
        return arg2
    elif arg2>arg1:
        print('sval: ',arg1)
        return arg1
    elif arg2 == arg1:
        print('sSameval: ',arg2)
        return arg2
    

for i in range(iterations):
    bVal=bigger(num1, num2)
    # print('bval: ',bVal)
    sVal = smaller(num1, num2)
    # print('sval: ',sVal)
    hVal=bVal/2
    print( 'hVal: ', hVal)
    if hVal<2:
        print('breaking loop: hval < 2')
        break
    elif hVal>=2:
        print('elif part of loop: hval >= 2')
        while(hVal>=2):
            hVal=bigger(hVal, sVal)
            hVal/=2
            print('inside while loop hVal: ', hVal)
