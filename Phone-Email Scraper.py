#!python3

"""
--------------------------------------------------------------------------------------------------------
Steps:
#START OF PROGRAM
#TODO: module
#TODO: Regex for phone number
#TODO: Regex for email ids
#TODO: Use Pyperclip to get the text from clipboard
#TODO: Extract phone numbers
#TODO: Extract email ids
#TODO: Paste the emails and phone numbers
#END OF PROGRAM

"""

#START OF PROGRAM

#Module

import re                          #re module regex or regular expression object 
import pyperclip                   #pyperclip module is used to copy paste the text from clipboard
#Regex for phone number
#Message For User
print("Hey User, Please Copoy The Whole Text From which You want to Extract the Phone Number And Emails")
print('WRITE YES WHEN YOU HAVE COPIED IT')
decission=input()
if decission.lower()!= 'YES':
    print('PLEASE COPY THE TEXT FIRST')
    print('Exitting !!!')
    exit(1)
phonenumber = re.compile(r'''
#PhonenNumber Actual format can be in: 798-789-7894, (789)-789-8794, (789) 789-7898, 789-7894, ext. 12345, x1232
(((\d\d\d)|(\(\d\d\d\)))?            #Area Code --- Here the first (\d\d\d) represent the area code without the parenthesis, second group (\(\d\d\d\)) this represents the area code with parenthesis. And ? Means that this can be either 1 or 0 time.
(\s|-)            #Dash/Seperator ------ Here \s means that it is a single space, - means can be seperated by a dash also
(\d\d\d)            #First 3 digits
(\s|-)            #Dash/Seperator
(\d\d\d\d)            #Last 4 Digits
((ext(\.)?\s|x)(\d{2,5}))?)      #Haven't included extension

''',re.VERBOSE)
#Regex for email ids
emailid = re.compile(r'''
#something@something, somethi.ng@something, som+ething@something, someth9ing@something, somethi_ng@something, someThing@something
[a-zA-Z0-9._+]+            #Username
@            #@ symbol
[a-zA-Z0-9._+]+             #domain

''',re.VERBOSE)
#Use Pyperclip to get the text from clipboard
rawtext = pyperclip.paste()                     #Pyperclip paste module menas that the text we have copied will be assigned to rawtext variabel as i have assigned.

#Extract email ids
ActualEmails = emailid.findall(rawtext)         #finding all sort of emails format in the raw text
#print(ActualEmails)                             #printing the emails that were found from the above result

#Extract phone numbers
ActualNumbers = phonenumber.findall(rawtext)         #finding the match type of phone number in the raw text
ExtractedPhoneNumbers = ['Extracted Phone-Emails']                           #created a empty list to store the phone numbers
for RawPhoneNumbers in ActualNumbers:                #Loop to find the full phone Nubmers 
    ExtractedPhoneNumbers.append(RawPhoneNumbers[0]) #Here i am joining the normal phone number to the list
#print(ExtractedPhoneNumbers)                         #printing the extracted phone number

#Proper Format For Phone Numebr And Email Ids
Result = '\n'.join(ExtractedPhoneNumbers) + '\n' + '\n'.join(ActualEmails)                              # here all the elements of the list will be now reformatted to new format that is in newline format as given argument is \n #'\n' in join fnction takes the argument that has to be done like in this case new line and .join function from list seperates comma to the argument that is given in quotes ahead.

#Paste the emails and phone numbers
pyperclip.copy(Result)                               #Here it will copy the results text into the clipboard


#Last Message to USER
print("Job Done Successfully ")
print('NOW GO TO ANY EDITOR AND PASTE...')
#END OF PROGRAM