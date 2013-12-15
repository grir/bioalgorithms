#!/usr/bin/env python3
###############################################################
import copy
import itertools
import collections




def readSpectrum(fileIn):
   fin = open(fileIn,"r")
   spec = []
   lines = fin.readlines()
   #print(lines)
   for lns in lines:
      wds = lns.split(' ')
      for k in wds:  
        spec.append(int(k.strip())) 
   return spec
   
###############################################################
def convolution(spectrum):
   spectrum.sort()
   cc = list(spectrum[1:])

   for i in range(1,len(spectrum)):
      for j in range(i+1,len(spectrum)):
         z = spectrum[j] - spectrum[i]
         if z > 0:
             cc.append(z)
   
   return cc      
         
###############################################################   
   

   
spectrum = readSpectrum("input.dat")
cc = convolution(spectrum)
for c in cc:
  print(c,end=" ")
  

