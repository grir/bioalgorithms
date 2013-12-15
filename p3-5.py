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
       
       if pp1 > pp and pp1 > 0:
          pp = pp1
          mostp = km   
    
    if pp == 0:
       mostp = allkm[0]  
              

    return mostp

########################################################  
def createProfileWithPseudocounts(motifset):
    #print(motifset)
    ll = len(motifset)
    k = len(motifset[0]) 
    probs = {}
    probs["A"] = []
    probs["C"] = []
    probs["G"] = []
    probs["T"] = []
    
    for i in range(0,k):
        sk = {}
        sk["A"] = ll
        sk["C"] = ll
        sk["G"] = ll
        sk["T"] = ll
         
        ll2 = ll * 2 

        for ch in range(0,ll):
           sk[ motifset[ch][i] ] = sk[ motifset[ch][i] ] + 1.0/ll2

        for ch in probs.keys():
            probs[ ch ].append( sk[ ch ] )  
        
    return probs


########################################################  
def scoreMotifs(motifset):
    ll = len(motifset)
    k = len(motifset[0])

    score = 0

    for i in range(0,k):
        sk = {}
        sk["A"] = 0.0
        sk["C"] = 0.0
        sk["G"] = 0.0
        sk["T"] = 0.0

        for ch in range(0,ll):
           sk[ motifset[ch][i] ] = sk[ motifset[ch][i] ] + 1

        big = max( [ sk["A"], sk["C"], sk["G"], sk["T"] ]) 

        score = score + ll - big
        
        
    return score

########################################################  

def printMotifs(motifset):
    for mot in motifset:
       print(mot)         

########################################################  
 
#GREEDYMOTIFSEARCH(Dna, k,t)
#   form a set of k-mers BestMotifs by selecting 1st k-mers in each string #from Dna
#        for each k-mer Motif in the 1st string from Dna
#            Motif1 ← Motif
#            for i = 2 to t
#                form Profile from motifs Motif1, …, Motifi - 1
#                Motifi ← Profile-most probable k-mer in the i-th string in Dna
#            Motifs ← (Motif1, …, Motift)
#            if Score(Motifs) < Score(BestMotifs)
#                BestMotifs ← Motifs
#        output BestMotifs






fin = open("input.dat","r")

ts = fin.readline()
kt = ts.split()
k = int(kt[0].strip())
t = int(kt[1].strip())


dna = []
dnaMotifs = []
bestMotifs = []

for i in range(0,t):
    line2 = fin.readline()
    line  = line2.strip()
    dna.append( line  )
    dnaMotifs.append( getKMers(dna[i], k))
    bestMotifs.append( dnaMotifs[i][0])


#print(dnaMotifs)
    
for mot1 in dnaMotifs[0]:
    motifs = [ mot1 ]
    for i in range(1,t):
       probs = createProfileWithPseudocounts(motifs)
   #    print(probs)
       moti = mostProb(dna[i], probs, k)
   #    print("--->", moti)
       motifs.append(moti)

    if scoreMotifs(motifs) < scoreMotifs(bestMotifs):
       bestMotifs =  motifs 

printMotifs( bestMotifs )
    
