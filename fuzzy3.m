clc;
clear all;

fis1 = readfis('first');
house = evalfis([50000,6],fis1);

fis2 = readfis('second');
applicant = evalfis([800050,60000],fis2);

fis3 = readfis('third');
Credit = evalfis([50000,6,applicant,house],fis3);

disp(Credit);