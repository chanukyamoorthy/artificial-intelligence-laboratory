clc;
clear all;

fis = readfis('second');
out = evalfis([800050,60000],fis)