* Module 3: Advanced SAS Procedure's;

*1;

*proc import datafile='/folders/myfolders/sasuser.v94/458_dataset_v2.0.csv' dbms=csv out=global_dataset replace;
*run;

data inf_globalsale1;

infile '/folders/myfolders/sasuser.v94/458_dataset_v2.0.csv' lrecl=60000 dsd firstobs=2;

informat Order_ID $30. Order_Date ddmmyy10. Ship_Date ddmmyy10. Customer_ID $15. Segment $15. City $15. 
State $15. Country $15. Category $15. Sales dollar.  Discount 1.1 Profit dollar.;

format Order_Date ddmmyy10. Ship_Date ddmmyy10.;

input Order_ID$ Order_Date Ship_Date Customer_ID$ Segment$ City$ State$ Country$ Category$ Sales Quantity 
Discount Profit;
run;

proc contents data=inf_globalsale1;
run;

proc means data=inf_globalsale1;
var Sales; /*2670.69*/
run;

proc format library= WORK.FORMATS;
value $sales_fmt '0'='-Average' '1'='+Average';
run;

data inf_globalsale2;
set inf_globalsale1;
format Sales_wrt_Average$10. ;
if Sales < 2670.69 then Sales_wrt_Average = '0';
if Sales > 2670.69 then Sales_wrt_Average = '1';
run;

data inf_globalsale3;
set  inf_globalsale2;

format Sales_wrt_Average sales_fmt;
run;

*proc catalog cat=WORK.formats;
*contents;
*run;

proc print data=inf_globalsale3;
run;

data inf_globalsale3;
set inf_globalsale2;
if Sales_wrt_Average = '0' then Sales_wrt_Average='-Average';
if Sales_wrt_Average = '1' then Sales_wrt_Average='+Average';
run;

proc print data=inf_globalsale3;
run;

proc surveyselect data=inf_globalsale3 method=srs seed=4 sampsize=10 out=global_samp;
run;

proc print data=global_samp;
run;

proc freq data=global_samp;
tables Sales_wrt_Average;
run;






