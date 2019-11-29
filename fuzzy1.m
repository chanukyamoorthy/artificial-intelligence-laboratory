clc;
clear all;

fis = readfis('first');
out = evalfis([500000,6],fis)