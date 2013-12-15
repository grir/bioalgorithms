#!/usr/bin/env python3

def getKMers(s, k):
   ll = len(s)
   kmers = [ ] 
   for i in range(0,ll-k+1):
        kmers.append(s[i:i+k])

   return kmers
    
#################################################################

def composition(string, k):
   comp = getKMers(string,k)
   comp.sort()
   return comp
   
#################################################################

def printList(mylist):
    for ll in mylist:
       print(ll)       

#################################################################


fin = open("input.dat","r")

ts = fin.readline()
kt = ts.split()
k = int(kt[0].strip())
dna = fin.readline()
dna = dna.strip()

llist = composition(dna,k)

printList(llist)
