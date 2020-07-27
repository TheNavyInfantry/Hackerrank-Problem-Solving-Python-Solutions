def timeConversion(userInp):
    if userInp[-2:] == 'AM' and userInp[:2] == '12': #Step for changing 12 into 00 in AM
        return '00'+userInp[2:-2]

    elif userInp[-2:] == 'AM': #Checking and deleting AM
        return userInp[:-2]

    elif userInp[-2:] == 'PM' and userInp[:2] == '12': #Checking if PM and if it is True, remove PM and return
        return userInp[:-2]

    else:
        return str(int(userInp[:2])+12)+userInp[2:8] #Adding 12 for Hour part which is index0 and index1

print(timeConversion('07:05:45PM'))


##EXTRA##


def timeConversion(userInp):

    splitInp = userInp.split(':') #Splitting user input

    if userInp[-2:] == 'PM': #checking if PM in user input
        if splitInp[0] != '12': #checking if first index (index0) 12 or not
            splitInp[0] = str(int(splitInp[0])+12) #adding 12 to index0 and converting to 24Hour-System

    else:
        if splitInp[0] == '12':#checking if first index (index0) 12 or not at AM
            splitInp[0] = '00' #If it is, changing from 12 into 00

    joinInp = ':'.join(splitInp) #Joining splitted parts
    return str(joinInp[:-2]) #Removing PM/AM part


print(timeConversion('07:05:45PM'))


def timeConversion(userInp):
    if userInp[-2:] == 'AM' and userInp[:2] == '12':
        return '00'+userInp[2:-2]

    elif userInp[-2:] == 'AM':
        return userInp[:-2]

    elif userInp[-2:] == 'PM' and userInp[:2] == '12':
        return userInp[:-2]

    else:
        return str(int(userInp[:2])+12)+userInp[2:8]