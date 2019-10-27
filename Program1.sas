/*To maximize the profit, check the products providing profit more than 40% of the
sale amount and increase the quantity of those products to 15. Also check, by what
amount do you need to increase the quantity (Consider the dataset inf_globalsale)*/

data inf_globalsale1;

infile '/folders/myfolders/sasuser.v94/458_dataset_v2.0.csv' lrecl=60000 dsd firstobs=2;

informat Order_ID $30. Order_Date ddmmyy10. Ship_Date ddmmyy10. Customer_ID $15. Segment $15. City $15. 
State $15. Country $15. Category $15. Sales dollar.  Discount 1.1 Profit dollar.;

format Order_Date ddmmyy10. Ship_Date ddmmyy10.;

input Order_ID$ Order_Date Ship_Date Customer_ID$ Segment$ City$ State$ Country$ Category$ Sales Quantity 
Discount Profit;
run;

*proc contents data=inf_globalsale1;
*run;

data inf_globalsale2;

set inf_globalsale1;

if Profit>Sales*0.4 then
Quantity_incresed = 15-Quantity;
if Profit>Sales*0.4 then
Quantity = 15 ;
run;

proc print data = inf_globalsale2;
run;
