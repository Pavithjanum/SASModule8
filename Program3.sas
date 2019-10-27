/*Don’t you see, there isn’t a ‘$’ sign in front of Profit Variables? Add the dollar sign
before the profit values and store them within a new variable named ‘Gain’. Also
make sure that the values don’t carry decimal places*/

data inf_globalsale4(rename=(Profit=Gain));

set inf_globalsale3;

format Sales dollar. Profit dollar.;

Sales=round(Sales);
Profit=round(Profit);
run;

proc print data = inf_globalsale4;
run;
