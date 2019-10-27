DATA global_stuffs;

infile cards dlm=',';

informat Cust_ID 10. Cust_Name$20. Cust_date ddmmyy10. amount;

input Cust_ID Cust_Name$ Cust_date amount;

format Cust_ID 10. Cust_Name$20. Cust_date ddmmyy10.  amount dollar12.;

Cards;
376020,Pavithra Ulaganathan,11-11-2016,2888
;

run;
