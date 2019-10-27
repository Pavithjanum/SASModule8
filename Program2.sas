DATA global_sales;
infile datalines dlm=",";

informat Order_ID $30. Order_Date $10. Ship_Date $10. Customer_ID $15. Segment $15. City $15. 
State $15. Country $15. Category $15. Sales $6. Quantity Discount Profit $6. ;

format Order_ID $30. Order_Date $10. Ship_Date $10. Customer_ID $15. Segment $15. City $15. 
State $15. Country $15. Category $15. Sales $6. Quantity Discount Profit $6. ;

input Order_ID$ Order_Date$ Ship_Date$ Customer_ID$ Segment$ City$ State$ Country$ 
Category$ Sales$ Quantity Discount Profit$;

datalines;
CA_2014_AB10015140_41954, 11-11-2014, 13-11-2014, AB_100151402, Consumer, Oklahoma City, Oklahoma, United_States, Technology, $221.98, 2, 0, $62.15
;

run;

proc print data=global_sales;
run;
