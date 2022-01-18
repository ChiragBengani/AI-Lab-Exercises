fever = input('Do you have Fever? (y/n) : ')
nose = input('Do you have a stuffy nose? (y/n) :')
smaste = input('Can you taste and smell? (y/n) :')
throat = input('Do you have sore throat/Does your throat hurt? (y/n) :')
body = input('Do you have any body ache? (y/n) :')
cough = input('Do you have cough? (y/n) :')

if fever=='n' and nose=='n' and smaste=='n' and throat=='n' and body=='n' and cough=='n':
    print('Diagnosis: You are completely fine')
elif fever=='y'and nose=='n' and smaste=='n' and throat=='n' and body=='n' and cough=='n':
    print('Diagnosis: You have a fever. Paracetamol Prescribed')
elif fever=='y' and nose=='y' and smaste=='n' and throat=='n' and body=='n' and cough=='n':
    print('Diagnosis: You have a cold. Combiflam prescried')
elif fever=='y' and nose=='y'and smaste=='y' and throat=='n' and body=='n' and cough=='n':
    print('Diagnosis: You might have COVID. Please get tested and till then isolate yourself.')
elif fever=='y' and nose=='y'and smaste=='y' and throat=='y' and body=='n' and cough=='n':
    print('Diagnosis: Chances of having COVID are high. Immedieately Consult your doctor and get tested.')
elif fever=='y' and nose=='y'and smaste=='y' and throat=='y' and body=='y' and cough=='n':
    print('Diagnosis: High chances of COVID. Please Isolate yourself immediately and consult your doctor')
elif fever=='y' and nose=='y'and smaste=='n' and throat=='y' and body=='y' and cough=='y':
    print('Diagnosis: You have COVID. Please isolate yourself and get in touch with your doctor immedieately.')
elif fever=='y' and nose=='y'and smaste=='n' and throat=='y' and body=='y' and cough=='y':
    print('Diagnosis: You have the flu. Please consult your doctor. Tamiflu prescribed')
elif fever=='n' and nose=='n'and smaste=='n' and throat=='y' and body=='n' and cough=='y':
    print('Diagnosis: You have a throat infection. Please consult an ENT Doctor immediately')
elif fever=='n' and nose=='n'and smaste=='n' and throat=='n' and body=='y' and cough=='n':
    freq = input('Is the body pain in a specific part or throught the body? \n (specific/throughout) :')
    if freq=='specific':
        print('You can use any analgesic(pain relieving) ointment on the affected area')
    else:
        print('Body pain throughout the body is a sign of early onsent of Arthritis. \n Please consult a physiotherapist')