#imports PyPDF2 module needed for the program
try:
    import PyPDF2 as pd

except ImportError as error: #installs the module using pip if it isn't installed yet
    import os
    os.system('pip install PyPDF2')

file_path = input('Enter pdf file path: ') #path to pdf file

#opens and reads the file
File  = open(file_path,'rb')
pdfReader = pd.PdfFileReader(File)

tried = 0 # sets number of trials to zero, increments 

if not pdfReader.isEncrypted: # checks whether the file is encrypted
    print('The File is not encrypted. You can open it')

else:
    wordlist = open(input('Enter path to wordlist: '),'r')
    if input('Is the password in \n(a)uppercase \n(b)lower case\n:').lower() == 'b':
        body =  wordlist.read()
    else:
        body = wordlist.read()
    
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        print('Trying Decryption using {}'.format(word))
        result = pdfReader.decrypt(word)
        if result == 1:
            print('PASSWORDS SUCCESSFULLY DECRYPTED\nThe Password is {}'.format(word))
            break
        
        else:
            tried += 1
            print('PAsswords Tried: '+ str(tried))
            continue


    