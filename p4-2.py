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
def suffix(string, k):
   s = ''
   for i in range(0, k):
       s = string[len(string) - i - 1] + s
   
   return  s

#################################################################
def prefix(string, k):
   s = ''
   for i in range(0, k):
       s = s + string[i]
   
   return  s
#################################################################

def isRelated(s1, s2):
   ll1 = len(s1)-1
   mx = 0
   #for i in range(ll1-1,ll1):
   #   print(suffix(s1,i),' ',prefix(s2,i))
   for i in range(0,ll1):
      if s1[i+1] != s2[i]:
         return mx
      else:
         mx = mx + 1    

   return mx
   
#################################################################

def printList(mylist):
    for ll in mylist:
       print(ll)       

#################################################################


fin = open("input.dat","r")

ts2 = fin.readlines()
ts=[]
for s in ts2:
   ts.append(s.strip())

ll = len(ts)
ll1 = len(ts[0])-1
for i in range(0,ll):
  # print(i)
   for j in range(0,ll):
      if i != j :
         if isRelated(ts[i],ts[j]) == ll1:
            print(ts[i],"->", ts[j]) 
            

