/*Q1: Read all the data within SAS from the downloaded CSV file, using INFILE statement:
• The resulting SAS dataset named ‘inf_globalsales’ should be permanent
• Include the different options used with the INFILE statement, wherever necessary*/

* Create permanent library;

libname SALES '/folders/myfolders/sasuser.v94';

data SALES.inf_globalsales;

infile '/folders/myfolders/sasuser.v94/458_dataset_v2.0.csv' delimiter=',' lrecl=32767 dsd  firstobs=2;

informat Order_ID $30. Order_Date Ship_Date Customer_ID $15. Segment $15. City $15. 
State $15. Country $15. Category $15. Sales $12.  Discount 1.1 Profit $12.;

Input Order_ID$ Order_Date Ship_Date Customer_ID$ Segment$ City$ State$ Country$ Category$ Sales Quantity 
Discount Profit;

format Order_ID$30. Order_Date ddmmyy10. Ship_Date ddmmyy10. Customer_ID$15. Segment$15. City$15. 
State$15. Country$15. Category$15. Sales dollar12.  Discount Profit dollar12;


run;

proc print data=sales.inf_globalsales;
run;

*Q2: Create a new dataset named imp_globalsales in SAS and import the former CSV dataset 
within SAS using PROC Import;

proc import datafile= '/folders/myfolders/sasuser.v94/458_dataset_v2.0.csv' dbms=csv out=imp_globalsales 
replace;

proc print data=imp_globalsales;
run;

/*Q3: Perform the use of KEEP, DROP and RENAME options in SAS:
• Create a new dataset keep_globalsale and use KEEP option to include the variables Order_ID, Order_Date, Ship_Date and Sales
• Create a new dataset drop_globalsale and use DROP option to include the variables Segment, Country, Category and Sales
• Create a new dataset rename_globalsale and rename the variable Segment to Class, such that the Class variable can be used for further processing*/

data keep_globalsale;
set imp_globalsales(keep=Order_ID Order_Date Ship_Date Sales);
run;

data drop_globalsale;
set imp_globalsales(drop=Segment Country Category Sales);
run;

data rename_globalsale;
set imp_globalsales(rename=(Segment=Class));
run;

proc print data=keep_globalsale;
run;

proc print data=drop_globalsale;
run;

proc print data=rename_globalsale;
run;


/*Q4: Perform the following tasks:
• Create a new dataset conc_globalsale and concatenate the datasets keep_globalsale and drop_globalsale
• Create a new dataset inter_globalsale and interleave the datasets keep_globalsale and drop_globalsale
• Create a new dataset comb_globalsale and combine the datasets keep_globalsale and drop_globalsale
• Create a new dataset merge_globalsale and merge the datasets keep_globalsale and drop_globalsale*/

data conc_globalsale;set keep_globalsale drop_globalsale ;run;

proc print data=conc_globalsale;run;

proc sort data=keep_globalsale;by Order_ID;run;

proc sort data=drop_globalsale;by Order_ID;run;

data inter_globalsale;set keep_globalsale drop_globalsale ;by Order_ID;run;

proc print data=inter_globalsale;run;

data comb_globalsale;set keep_globalsale;set drop_globalsale;run;

proc print data=comb_globalsale;run;

data merge_globalsale;merge keep_globalsale drop_globalsale;run;

proc print data=merge_globalsale;run;








