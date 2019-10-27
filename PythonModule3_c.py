# -*- coding: utf-8 -*-

"""

Created on Thu May 23 19:29:47 2019

 

@author: 376020

""" 

import csv

import re

#import CustomerNotAllowedException 

 

class Error(Exception):

    pass

    

class CustomerNotAllowedException(Error):

    '''blacklisted entry..not allowed here!!..Raised CustomerNotAllowedException'''

    pass

 

class Customer:

 

    '''Integrating customer databases of GoodsKart and FairDeal organizations '''

    

    def __init__(self,title=None,fname=None,lname=None,isblacklisted=0):

        self.title = title

        self.fname = fname

        self.lname = lname

        self.isblacklisted = isblacklisted

        

    def gettitle(self):

        return self.title

        

    def get_fname(self):

        return self.fname

    

    def get_lname(self):

        return self.lname

    

    def get_isblacklisted(self):

        return self.isblacklisted

            

    def set_title(self,title):

        self.title = title

        

    def set_fname(self,fname):

        self.fname = fname

        

    def set_lname(self,lname):

        self.lname = lname

        

    def set_isblacklisted(self,isblacklisted):

        self.isblacklisted = isblacklisted

        

    def datacontent(self,path):

        datacontent = []

        with open(path,'r') as data:

            content = csv.reader(data,delimiter=',',quotechar='|')

            for row in content:

                datacontent.append([row[1],row[2]])

        return datacontent

    

    def createOrder(self,datacontent):

        nametitle=''

        firstname=''

        lastname=''

        namelist=[]

        regex_pattern = re.compile(r" (?P<title_name>\w+)\. (?P<first_name>\w+) (?P<last_name>\w+)")

        for row in datacontent:

            m = regex_pattern.search(row[0])

            if m != None:

                nametitle = m.group('title_name')

                firstname = m.group('first_name')

                lastname = m.group('last_name')

                #print(nametitle,firstname,lastname)

                try:

                    if int(row[1]) == 0:

                        namelist.append([nametitle,firstname,lastname,row[1]])

                    else:

                        raise CustomerNotAllowedException

                        

                except CustomerNotAllowedException:

                    print('CustomerNotAllowedException due to backlisted customer entry')

        return namelist

 

            


 

 

# -*- coding: utf-8 -*-

"""

Created on Thu May 23 18:54:42 2019

 

@author: 376020

"""

 

#Domain – E-Commerce 

#focus – Optimization 

#Business challenge/requirement 

#GoodsKart—largest ecommerce company of Indonesia with revenue of $2B+ acquired another ecommerce company FairDeal. 

#FairDeal has its own IT system to maintain records of customer, sales etc. For ease of maintenance and cost savings GoodsKart 

#is integrating customer databases of both the organizations hence customer data of FairDeal has to be converted in GoodsKart Customer 

#Format. 

#Key issues 

#GoodsKart customer data has more fields than in FairDeal customer data. Hence FairDeal data needs to be split and stored 

#in GoodsKart Customer Object Oriented Data Structure 

#Considerations 

#System should convert the data at run time 

#Data volume 

#- NA 

#Additional information 

#- NA 

#Business benefits 

#GoodsKart can eventually sunset IT systems of FairDeal and reduce IT cost by 20-30% 

#Approach to Solve 

#You have to use fundamentals of Python taught in module 3. 

#1. Read FairDealCustomerData.csv 

#2. Name field contains full name – use regular expression to separate title, first name, last name 

#3. Store the data in Customer Class 

#4. Create Custom Exception – CustomerNotAllowedException 

#

#

#5. Pass a customer to function "createOrder" and throw CustomerNotAllowedException in case of blacklisted value is 1 

#Enhancements for code 

#You can try these enhancements in code 

#1. Change function createOrder to take productname and product code as input 

#2. Create Class Order 

#

#Return object of type Order in case customer is eligible

 

import Customer

 

ob = Customer.Customer()

pathname = r'C:\Users\376020\Desktop\Masters\Python\Module3\datasets\FairDealCustomerData.CSV'

 

Fairdeal_data = []

formatted_data =[]

Fairdeal_data = ob.datacontent(pathname)

 

#print(Fairdeal_data)

 

formatted_data = ob.createOrder(Fairdeal_data)

print(formatted_data)
