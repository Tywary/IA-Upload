from internetarchive import *
import os
import time



def user_input():
    global collectionname, title, typem, identifier, accesskey, secretkey, list_of_files, file, mdata, status
    status = 0
    Prompt = None

    while Prompt not in ("yes", "y", "n", "no"): #loop
            Prompt = input("Do you wish to add multiple files? y/n ")
            if Prompt in ('y', 'yes'):
                state = 1
            elif Prompt in ('n', 'no'): 
                state = 2

    while state in (1, 2, 3):
        if state == 2:
            file = input("Enter File Location: ")
            if os.path.exists(file):
                print('The file path exists \n')
            else:
                print("The specified file path doesn't exist ")
                state = 2
            collectionname = str(input("Collection Name: "))
            title = str(input("Title: "))
            typem = str(input("Media Type: "))
            identifier = input("A Unique Identifier: ")
            accesskey = input("Your Access Key: ")
            secretkey = input("Your Secret Key: ")
            mdata = {'Collection': collectionname, 'title': title, 'mediatype': typem}
            uploading_single()
            

        elif state == 1:
            global list_of_files
            list_of_files = []
            file = input("Enter File Location: ")
            if os.path.exists(file):
                print('The file has been added\n')
                list_of_files.append(file)
                Prompt2 = None
                while Prompt2 not in ("yes", "y", "n", "no"): #loop
                    Prompt2 = input("Do you want to add more files? y/n ")
                    if Prompt2 in ('y', 'yes'):
                        state = 1
                    elif Prompt2 in ('n', 'no'): 
                        state = 3
                    else:
                        print('Invalid Input')
            else:
                print("The specified file path doesn't exist \n")
                state = 1
                
        elif state == 3:
            collectionname = str(input("Collection Name: ")) #test_collection
            title = str(input("Title: ")) 
            typem = str(input("Media Type: ")) # texts etree audio movies software image data web collection account
            identifier = input("A Unique Identifier: ")
            accesskey = input("Your Access Key: ")
            secretkey = input("Your Secret Key: ")
            mdata = {'Collection': collectionname, 'title': title, 'mediatype': typem}
            uploading_multi()



def upload_multiple():
    global status
    status = 0
    r = upload(identifier, files=list_of_files, metadata=mdata, access_key=accesskey, secret_key=secretkey)
    print(f"status code: {r[0].status_code}")
    if r[0].status_code != 200:
        status += 1
    if r[0].status_code == 200:
        status += 2
    

def upload_single():
    global status
    status = 0
    r = upload(identifier, files=file, metadata=mdata, access_key=accesskey, secret_key=secretkey)
    print("status code: ")
    print(r[0].status_code)
    if r[0].status_code != 200:
        status += 1
    if r[0].status_code == 200:
        status += 2


def uploading_single():
    global status
    status = 0
    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    i = 0
    upload_single()
    while status != (1, 2):
        i = (i + 1) % len(symbols) #disabled
        print('\r\033[K%s Uploading 1 file...' % symbols[i], flush=True, end='')
        time.sleep(0.1)
        if status == (1, 2):
            break
        
    if status == 2:
        url = "https://archive.org/details/"+str(identifier)
        print('Successfully Uploaded!')
        print('The Uploaded item will be available at this url: '+ url)
        print("\n")
        __init__()
            
    elif status == 1:
        print('Error occurred')
        print("Refer to the status code to understand the exception: \n\n")
        __init__()
        
            
def uploading_multi():
    n = len(list_of_files) + 1
    status = 0
    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    i = 0
    upload_multiple()
    while status != (1, 2):
        i = (i + 1) % len(symbols) #disabled
        print(f'\r\033[K%s Uploading {n} file(s)...' % symbols[i], flush=True, end='')
        time.sleep(0.1)
        if status == (1, 2):
            break
        
    if status == 2:
        url = "https://archive.org/details/"+str(identifier)
        print('Successfully Uploaded!')
        print('The Uploaded item will be available at this url: '+ url)
        print("\n")
        __init__()
            
    elif status == 1:
        print('Error occurred')
        print("Refer to the status code to understand the exception: \n\n")
        __init__()
        
    
def __init__():

    print(r"""                ██╗███╗░░██╗████████╗███████╗██████╗░███╗░░██╗███████╗████████╗
                ██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗████╗░██║██╔════╝╚══██╔══╝
                ██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝██╔██╗██║█████╗░░░░░██║░░░
                ██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██║╚████║██╔══╝░░░░░██║░░░
                ██║██║░╚███║░░░██║░░░███████╗██║░░██║██║░╚███║███████╗░░░██║░░░
                ╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝░░░╚═╝░░░
    
                ░█████╗░██████╗░░█████╗░██╗░░██╗██╗██╗░░░██╗███████╗
                ██╔══██╗██╔══██╗██╔══██╗██║░░██║██║██║░░░██║██╔════╝
                ███████║██████╔╝██║░░╚═╝███████║██║╚██╗░██╔╝█████╗░░
                ██╔══██║██╔══██╗██║░░██╗██╔══██║██║░╚████╔╝░██╔══╝░░
                ██║░░██║██║░░██║╚█████╔╝██║░░██║██║░░╚██╔╝░░███████╗
                ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝
    
                ██╗░░░██╗██████╗░██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
                ██║░░░██║██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                ██║░░░██║██████╔╝██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝
                ██║░░░██║██╔═══╝░██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗
                ╚██████╔╝██║░░░░░███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║
                ░╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝""")
    print(' Start - 1 \n Exit - 2')
    promp = None
    while promp != (1, 2):
        promp = int(input('Enter 1 to start or 2 to exit: '))
        if promp == 1:
            user_input()
        elif promp == 2:
            exit()
        else:
            print('Invalid Input')
            
    
__init__()