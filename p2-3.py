#!/usr/bin/env python3
def compl( rna ):
   ss = ""
   for i in range(0,len(rna)):
      ss = ss + cmpl[ rna[i] ]
   return ss   

def toProtein(ss, cds):
    prot = ""
    ll = len(ss)
    for i in    range(0,ll,3):
        prot = prot + cds[ss[i:i+3]]
    return prot

def toRNA(ss):
    rna = ""
    ll = len(ss)
    for i  in    range(0,ll):
        if ss[i] == 'T':
           rna = rna + 'U'
        else:
           rna = rna + ss[i]       
        
    return rna



def reverseCompl(rna):
    ss = compl(rna)
    ll = len (ss)
    ss1 = "" 
    for i in range(0,ll):
        ss1 = ss[i] + ss1   
    return ss1    

def getCDS():
    fin = open("codons.dat","r")
    lines = fin.readlines()
    cds = {}
    for lns in lines:
        wds = lns.split(' ')
        cds[wds[0].strip()]=wds[1].strip()
    return cds 


def getMass():
    fin = open("acmass.dat","r")
    lines = fin.readlines()
    cds = {}
    for lns in lines:
        wds = lns.split(' ')
        cds[wds[0].strip()] = int(wds[1].strip())
    return cds 

# returns a part of cyclic peptide 
def getPart(cpept, fromA, length):
    ss=""
    ll = len(cpept)
    for i in range(0, length):
       ss = ss + cpept[ (fromA + i) % ll ]
    
    return ss  

# returns the mas of protein

def getPepMass(s, acmass):
    m = 0
    for i in range(0, len(s)):
       m = m + acmass[ s[i] ]
    
    return m


       
    








cmpl = {'A':'U', 'C':'G', 'G':'C', 'U': 'A'}
#------------------------------------------------------

#cpept ="LEQN"
cpept ="GMCNEEDAGLRLVKR"
ll=len(cpept)
#print (ll)
acmass = getMass()

spectra = {"":0, cpept:getPepMass(cpept, acmass)}
vals = [0, getPepMass(cpept, acmass)]


for length in range(1,ll):
   for start in range(0,ll):
      ss = getPart(cpept, start, length)
#      print(ss)
      vals.append(getPepMass(ss, acmass))

vals.sort()



for m  in vals:
   print(m, end=' ')
   
print()   

