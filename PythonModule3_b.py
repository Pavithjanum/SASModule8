# -*- coding: utf-8 -*-

"""

Created on Thu May 23 15:12:47 2019

 

@author: 376020

"""

import csv

 

class Customer:

    ''' To come up with program which reads the file and builds a set of unique profession list and given input profession of client – 

    system tells whether client is eligible to be approached for marketing campaign. '''

    

    def __init__(self,title=None,fname=None,lname=None,isblacklisted=None,profession=None,age=None):

        self.title = title

        self.fname = fname

        self.lname = lname

        self.isblacklisted = isblacklisted

        self.profession = profession

        self.age = age

        

    def settitle(self,title):

        self.title = title

    

    def setfname(self,fname):

        self.fname = fname

        

    def setlname(self,lname):

        self.lname = lname

        

    def set_isblacklisted(self,isblacklisted):

        self.isblacklisted = isblacklisted 

    

    def set_profession(self,profession):

        self.profession = profession 

    

    def set_age(self,age):

        self.age = age 

        

    def gettitle(self):

        return self.title

    

    def getfname(self):

        return self.fname

    

    def getlname(self):

        return self.lname

    

    def get_isblacklisted(self):

        return self.isblacklisted

    

    def get_profession(self):

        return self.profession

    

    def get_age(self):

        return self.age

        

    def readdata(self,filename):

        datacontent=[]

        with open(filename,'r') as data:

            content = csv.reader(data,delimiter=',',quotechar='|')

            for i,j in enumerate(content,start=1):

                if i>1:

                    datacontent.append([j[0],j[1],j[2],j[3]])

        return datacontent   

 

    def uniquejobs(self,datacontent):

        alljobs=[]

        uniquejobs={}

        for row in datacontent:

            alljobs.append(row[1].lower())

        uniquejobs = set(alljobs)

        return uniquejobs

    

    def eligible_age(self,datacontent):

        ages=[]

        eligible_age={}

        for row in datacontent:

            ages.append(row[0])

            

        eligible_age['Max_age'] = max(ages)

        eligible_age['Min_age'] = min(ages)

        return eligible_age

    

    def age_check(self,age,eligible_age):

        #print(eligible_age['Min_age'],eligible_age['Max_age'],int(age))

        if ((int(eligible_age['Min_age'])) <= int(age) <= int((eligible_age['Max_age']))):

            return 'eligible'

        else:

            return 'not eligible'

    

    def profession_check(self,profession,uniquejobs):

        if profession.lower() in uniquejobs:

            return 'eligible'

        else:

            return 'not eligible'

    

    

    


    

 

# -*- coding: utf-8 -*-

"""

Created on Thu May 23 14:54:43 2019

 

@author: 376020

"""

#

#Domain – Banking Marketing 

#focus – Optimization 

#Business challenge/requirement 

#Bank of Portugal runs marketing campaign to offer loans to clients. Loan is offered to only clients with particular professions. 

#List of successful campaigns (with client data) is given in attached dataset. You have to come up with program which reads the file 

#and builds a set of unique profession list and given input profession of client – system tells whether client is eligible to be 

#approached for marketing campaign. 

#Key issues 

#Tele Caller can only make x number of cold calls in a day. Hence to increase her effectiveness only eligible customers should be called 

#Considerations 

#Current system does not differentiate clients based on age and profession 

#Data volume 

#447 records in bank-data.csv 

#Additional information 

#- NA 

#Business benefits 

#Company can achieve between 15% to 20% higher conversion by targeting right clients 

#Approach to Solve 

#You have to use fundamentals of Python taught in module 3 

#1. Read file bank-data.csv 

#2. Build a set of unique jobs 

#3. Read the input from command line –profession 

#4. Check if profession is in list 

#5. Print whether client is eligible 

#

#Refer to CheckForProfessionEligibility.py for solution and bank-data.csv for data 

#Enhancements for code 

#You can try these enhancements in code 

#1. Compute max and min age for loan eligibility based on data in csv file 

#2. Store max and min age in dictionary 

#3. Make the profession check case insensitive 

#4. Currently program ends after the check. Take the input in while loop and end only if user types "END" for profession 

 

import Customer

 

ob = Customer.Customer()

 

bankdetails = []

bankdetails = ob.readdata(r'C:\Users\376020\Desktop\Masters\Python\Module3\datasets\bank-data.csv')

print(bankdetails)

 

uniquejobs = ob.uniquejobs(bankdetails)

print(uniquejobs)

 

eligible_age = ob.eligible_age(bankdetails)

print(eligible_age)

 

while True:

    option = input('''Welcome to Bank of Portugal marketing campaign to offer loans to clients\n1. To Enter your details\n2. To know eligible profession lists?\n3. To know eligible age limits?\n4. To End this active session\nChoose youroption :''')

    

    if int(option) == 1:

        title = input('Enter your title(Mr/Mrs/Miss): ')

        fname = input('Enter your first name: ')

        lname = input('Enter your last name: ')

        profession = input('Enter your profession: ')

        age = int(input('Enter your age: '))

        isblacklisted = 'No'

        

        if (title != '' and fname != '' and lname != '' and profession != '' and age != ''):

            ab = Customer.Customer(title,fname,lname,isblacklisted,profession,age)

            eligible_ind = ab.profession_check(ab.get_profession(),uniquejobs)

            if eligible_ind == 'eligible':

                #print('Profession eligibiity satisfied')

                age_eligible_ind = ab.age_check(ab.get_age(),eligible_age)

                if age_eligible_ind == 'eligible':

                    #print('Age eligibiity satisfied')

                    print('Bank employees will contact you shorlty for processing your request. Please wait for a while!\n')

                    print('Your details: '+str(ab.gettitle())+'.'+str(ab.getfname())+' '+str(ab.getlname())+' with age '+str(ab.get_age())+' holding the current profession as '+str(ab.get_profession())+' !!!!...')

                else:

                    print('Sorry! Age eligibiity not satisfied')

                    break

            else:

                print('Sorry! Profession eligibiity not satisfied')

                break

 

    elif int(option) == 2:

        print('Eligible professionals are as follows\n')

        for entry in uniquejobs:

            print(entry)

    

    elif int(option) == 3:

        print('Eligible age limit is from %s to %s ' %(eligible_age['Min_age'],eligible_age['Max_age']))

        

    elif int(option) == 4:    

        terminate_option = input('Please confirm by typing "END", to quit: ')

        if terminate_option.lower() == 'end':

            break

        else:

            print('Didn\'t receive END response from you!..try again')
