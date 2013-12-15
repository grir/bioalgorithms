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

def getDeBrujn(kmers):
   ll = len(kmers)
   k = len(kmers[ 0 ]) 
   deBrujn = {}
   
   for i in range(0, ll-1):
      s = kmers[ i ][0:k-1]
      deBrujn[s] = [ ]
   
   for i in range(0, ll-1):
      s = kmers[ i ][0 : k-1]
      t = kmers[ i ][1 : k]
      deBrujn[s].append(t) 
      

   return deBrujn
   
#################################################################

def printList(mylist):
    for ll in mylist:
       print(ll)       

#################################################################
def printDeBrujn(deBrujn):
    for node in deBrujn.keys():
       print(node,"->", end=' ')
       llist = deBrujn[ node ]
       ll = len(llist)
       for i in range(0,ll):
          if i != (ll-1):
             print(llist[i],end='')
             print(',',end='')
          else:
             print(llist[i])
               

#################################################################

fin = open("input.dat","r")

ts = fin.readline()
k = int(ts.strip())


ts2 = fin.readline()
s = ts2.strip()

kmers = getKMers(s, k)

deBrujn = getDeBrujn(kmers)

printDeBrujn(deBrujn) 

