*2;

proc corr data=inf_globalsale3;
var Sales Profit;
run;

proc means data=inf_globalsale3;
class Sales_wrt_Average;
var Sales Profit;
run;

proc summary data=inf_globalsale3 print;
class Sales_wrt_Average;
var Sales Profit;
run;

proc rank data=inf_globalsale3 out=inf_globalrank groups=3;
var Profit; ranks global_rank;
run;

proc sort data=inf_globalrank;
by global_rank;
run;

proc print data=inf_globalrank;
run;

