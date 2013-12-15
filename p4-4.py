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

def getDeBrujn2(kmers):
   ll = len(kmers)
   k = len(kmers[ 0 ]) 
   deBrujn = {}
   
   for i in range(0, ll):
      s = kmers[ i ][0:k-1]
      deBrujn[s] = [ ]
  
#   for i in range(0, ll):
#      s = kmers[ i ][1:k]
#      deBrujn[s] = [ ]
  
   
   for i in range(0, ll):
      for j in range(0, ll):
         if i != j:
            s1 = kmers[ i ] 
            t1 = kmers[ j ] 
            s = s1[1 : k]     #suffix
            t = t1[0 : k-1]   #prefix
            
#            if s == 'CGTCGCGAG':
#               print('Radome ',i,':', s1,'j: ', j, ' ',t1, ' s:', s, ' t:',t)

            if s == t:            
               #print(s1,"->",t1)
               ss = s1[0:k-1]
               tt = t1[0:k-1]
               deBrujn[ss].append(tt) 
               #print (deBrujn[s1[0:k-1]])
               if ss == 'CGTCGCGAG':
                   print('Radome')

   return deBrujn
   
#################################################################
def getDeBrujn3(kmers):
   ll = len(kmers)
   k = len(kmers[ 0 ]) 
   deBrujn = {}
   
   suffix = []
   for i in range(0, ll):
      suffix.append(kmers[ i ][1:k])
 
   ssuffix = set(suffix)
   
   prefix = []
   for i in range(0, ll):
      prefix.append(kmers[ i ][0:k-1])
 
   sprefix = set(prefix)
   
   lsuf = list(ssuffix)
   lpre = list(sprefix)
   
    
   for i in range(0, ll):
      s = kmers[ i ][0:k-1]
      deBrujn[s] = [ ]
  
   for suf in lsuf:
      deBrujn[s] = [ ]
  
   for suf in lsuf:
      for pre in lpre:
         if suf == pre:
            deBrujn[suf].append(pre)
   
   

   return deBrujn
   
#################################################################
def printList(mylist):
    for ll in mylist:
       print(ll)       

#################################################################
def printDeBrujn(deBrujn):
    llist = list(deBrujn.keys())
    llist.sort()
    for node in llist:
    #for node in deBrujn.keys():
       llist2x = deBrujn[ node ]
       lsetx = set(llist2x)  
       llist2 = list(lsetx)
       llist2.sort()
       ll = len(llist2)
       if ll > 0:
           print(node,"->", end=' ')
           for i in range(0,ll):
             if i != (ll-1):
               print(llist2[i],end='')
               print(',',end='')
             else:
               print(llist2[i])
               

#################################################################

fin = open("input.dat","r")

kmers = [] 
ts = fin.readlines()
for s in ts:
   kmers.append(s.strip())


#print(len(kmers)) 


deBrujn = getDeBrujn2(kmers)
print(deBrujn['CGTCGCGAG'])
#printDeBrujn(deBrujn) 
#print(deBrujn)

