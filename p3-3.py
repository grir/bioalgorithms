#!/usr/bin/env python3

##########################################################       
def getFloats(string):
   numbers_str = string.split()
   numbers_float = [float(x) for x in numbers_str]   
   return numbers_float


########################################################   
def  getProb(kmer, probs):
   prod = 1.0
   ll = len(kmer)
   for i in range(0,ll):
      ch = kmer[i]
      prod = prod * probs[ch][i]  
   
   return prod   
########################################################################           
def getKMers(s, k):
   ll = len(s)
   kmers = [ ] 
   for i in range(0,ll-k+1):
        kmers.append(s[i:i+k])

   return kmers
    

########################################################  
def mostProb(s, probs, t):
    mostp = ""
    pp = 0
    allkm = getKMers(s, t)
    
    for km in allkm:
       pp1 = getProb(km, probs) 
       if pp1 > pp:
          pp = pp1
          mostp = km   

    return mostp

########################################################  
 

fin = open("input.dat","r")
dna2 = fin.readline()
dna = dna2.strip()

ts = fin.readline()
t = int(ts.strip())

charss = fin.readline()
charss2 = charss.strip()

chars = charss.split()
print(chars)
probs = {}

for ch in chars:
   probs[ch] = []

for i in range(0,t):
   line = fin.readline()
   floats = getFloats(line)
   ff = 0
   for ch in chars:
      probs[ch].append(floats[ff])
      ff = ff + 1
   
print( mostProb(dna, probs, t))
    
