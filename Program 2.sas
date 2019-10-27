/*Obtain a regression equation between sales, profit and discount to model sales with respect to 
profit and discount (Use Logistic Regression, if necessary) */

proc reg data=inf_globalrank;
model Sales = Profit Discount;
run;

* R squared = 0.5673 and Adj R-Sq = 0.5132;


proc logistic data = inf_globalrank desc;
model Sales = Profit Discount;
run;

* Percent Concordant =73.1 and Percent Discordant=26.9;