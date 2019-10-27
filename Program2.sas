/*Use Arrays to perform the same operation as above and increase the quantity
accordingly*/

data inf_globalsale3;
array globalarray(4) Profit Sales Quantity Quantity_incresed;

set inf_globalsale1;

if globalarray(1)>globalarray(2)*0.4 then
globalarray(4) = 15-globalarray(3);
if globalarray(1)>globalarray(2)*0.4 then
globalarray(3) = 15 ;
run;

proc print data = inf_globalsale3;
run;
