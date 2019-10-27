data FirstProgram;
input Country$ State$ Id;
informat Country $15. ,State $15. ;
datalines;  *Cards
India TamilNadu 376020
USA Greenvillee 112768
UK London 783744
;
run;

proc print data=firstprogram;
run;
