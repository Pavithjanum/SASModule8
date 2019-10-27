*Q1;
data inf_globalsale2;

set inf_globalsale1;

if Profit>Sales*0.4 then
Quantity_incresed = 15-Quantity;
if Profit>Sales*0.4 then
Quantity = 15 ;
run;

%let var = Sales*0.4;
data reuse_ds;
set inf_globalsale1;
if Profit>&var then
Quantity_incresed = 15-Quantity;
if Profit>&var then
Quantity = 15 ;
run;

proc print data=reuse_ds;
run;

*Q2;

%macro univariate(dataset_name,var);
proc univariate data=&dataset_name;
var &var;
run;
%mend;

%univariate(reuse_ds,Profit)

