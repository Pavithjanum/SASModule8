/*Find the optimum number of groups and categorize different Order_ID’s having similar Sales, Profit and 
Discount. Obtain a dendogram within a dataset named clus_globalsale, to show the formation of each group*/

proc fastclus data=inf_globalrank maxc=2 maxiter=100 out=inf_globalclus;
var Sales Profit Discount;
run;

proc fastclus data=inf_globalrank maxc=3 maxiter=100 out=inf_globalclus;
var Sales Profit Discount;
run;

proc fastclus data=inf_globalrank maxc=4 maxiter=100 out=inf_globalclus;
var Sales Profit Discount;
run;

proc fastclus data=inf_globalrank maxc=5 maxiter=100 out=inf_globalclus;
var Sales Profit Discount;
run;

proc fastclus data=inf_globalrank maxc=6 maxiter=100 out=inf_globalclus;
var Sales Profit Discount;
run;

* Thus, the optimum number of groups = 4;

proc cluster data=inf_globalrank method=centroid rmsstd outtree=clus_globalsale;
var Sales Profit Discount;
run;