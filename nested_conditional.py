
name='sa'
phone='017075560006'
email=''
if(len(name)!=0 and len(phone)!=0 and len(email)!=0):
    print('failed')

else:
    if(len(name)<2  or len(name)>6):
        print('the name lemth must be between 2 and 6')
    elif(len(phone)<11):
        print('phone number must be 11')
    else:
        print('success')