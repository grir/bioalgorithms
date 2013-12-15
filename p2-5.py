#!/usr/bin/env python3
###############################################################
import copy
import itertools
import collections


def getMasses():
    fin = open("acmass2.dat","r")
    lines = fin.readlines()
    masses = []
    for lns in lines:
        wds = lns.split(' ')
        masses.append(int(wds[1].strip()))
     
    return masses 

###############################################################

def getPartMassList(listP, start, length):
    m = 0
    for i in range(0, length):
       m = m + listP[ (start + i ) % len(listP) ]
    
    return m

###############################################################

def expandList( pepList, masses, spectrumCounter ):
    new = []
    nw = {}
    for m in masses:
       for k in pepList: 
          kk = collections.deque(k)
          for rot in range(0,len(kk)):
             kkk = list(kk)
             kkk.append(m)
             if isConsistent(kkk, spectrumCounter):
                 lkkk = list(kkk)
                 tkkk = tuple( kkk )
                 if not tkkk in nw.keys():
                    new.append(lkkk)
                    nw[tkkk]=1           
             kk.rotate(1)
                 
          #print(new)
    return new
###############################################################

def expandList2( pepList, masses):
    new = []
    
    for m in masses:
       for k in pepList: 
          kk = list(k)
          kk.append(m)
          new.append(kk)
    return new
###############################################################


def createList( pepList, masses, spectrumCounter ):
    for m in masses:
       for i in range(0,spectrumCounter[m]):
          pepList.append( [m] )
        
    
###############################################################

def getSpectrumByMass(massList):
    #massList.sort()
    ll=len(massList)
    vals = [0, getPartMassList(massList,0,ll)]
    for length in range(1,ll):
     for start in range(0,ll):
       ss = getPartMassList(massList, start, length)
       vals.append(ss)

    #vals.sort()
    return vals 
###############################################################
def counter(lst):
    c1 = {}
    for m in lst:
      c1[ m ] = 0
    
    for m in lst:
      c1[ m ] = c1[ m ] + 1
    
    return c1
##############################################################
def getConsistentMasses(masses, spectrum):
    c1 = set(spectrum)   
    newmass = []
    for m in masses:
       if m in c1:
          newmass.append(m)
    
    return newmass       
##############################################################

def getLinearSpectrum(massList):
    spc = list(massList)
    ll = len(massList) 
    for k in range(1,ll):
      for pos in range(0, ll - k): 
          s = sum(massList[pos:pos+k+1])
          spc.append(s)       
    spc.sort()      
    return spc
    
##############################################################
def isConsistent(massList, spectrumCounter):
    if len(massList) > len(spectrumCounter.keys()):
       return False
    
    massListSpectrum = getLinearSpectrum(massList)
       
    c1 = counter(massListSpectrum)
    for m in massListSpectrum:
       if m not in spectrumCounter.keys():
          return False
       elif c1[ m ] > spectrumCounter[ m ] :
          return False
    
    return True
    
        
###############################################################

def outputMList(mlist):
   s=""
   for i in range(0,len(mlist)-1):
      s=s+""+str(mlist[i])+'-'
   s=s+str(mlist[len(mlist)-1])   
   print(s,end=' ')
        
###############################################################

def outputList(mlist):
   if len(mlist)==0:
      return; 
   
   s=""
   for i in range(0,len(mlist)-1):
      s=s+""+str(mlist[i])+'-'
   s=s+str(mlist[len(mlist)-1])   
   print(s,end=' ')

###############################################################

def CykloSeq(spectrum):
   l1 = [ ]
   masses = getMasses()
   masses = getConsistentMasses(masses, spectrum)
   
   print(masses)
   
   spectrumCounter = counter(spectrum)
   createList(l1, masses, spectrumCounter)
   print(l1)
   
   #l1 = [[0]]
   answer = []
   
#   l1.append(masses) 
#   print(l1)
   while len( l1 ) != 0 :
      l1 = expandList(l1, masses, spectrumCounter)
      print( len(l1), ' ', len(l1[0]) )
      todel = []
      for i in range(0,len(l1)):
          todel.append(True)
    #  print(todel)
          
      for i in range(0,len(l1)):
         mlist = l1[i]
         spc = getSpectrumByMass(mlist)
         spc.sort() 
       #  print("spc",spc)
         if spc == spectrum:
            outputMList(mlist)
#            answer.append(mlist)
            todel[i] = False
      nl1 = []
       
      for i in range(0, len(l1)):
          if todel[i]:
             nl1.append( l1[i])   
       
      l1 = nl1
 
 
########################################################### 
def getScores(pepList, spectrum):
    scores = []
    for i in range(0,len(pepList)):
       massListSpectrum = getSpectrumByMass(pepList[i])
#       print(" i=", massListSpectrum)
       c1 = counter(massListSpectrum)
       c2 = counter(spectrum)
       cs = 0
       if max(massListSpectrum) > max(spectrum):        
          cs = -1
       else:
          for m in massListSpectrum:
             if m  in c2.keys():
                cs = cs + min(c1[ m ],c2[ m ])

       scores.append(cs);
    
    return scores

########################################################### 
def Cut(l1, scores, spectrum, N): 
    newL1 = []
    scores_n = list(scores)
    scores_n.sort(reverse=True)
   
   # print(scores_n)
   
    i = 0
    while i in range(0, min(N,len(l1))):
       tos =  scores_n[ i ] 
       found = False
       for v in range(0,len(scores)):
          if scores[v] >= 0 and scores[v] == tos:
             newL1.append(l1[v]) 
             i = i + 1
             found = True
             if not i in range(0, min(N,len(l1))):
                break
       if not found:
          i = i + 1       

    return newL1


########################################################### 
 
 
def LeaderBoardCyclopeptideSequencing(spec):

   N = spec[0]
   print("N=",N)
   spectrum = spec[1:]
   spectrum.sort()
   
   maxmass = max(spectrum)
  
   #print("Spectrum :", spectrum, " ", max(spectrum)) 
      
   l1 = [ ]
   masses = getMasses()
   #masses = getConsistentMasses(masses, spectrum)
   for m in masses:
      l1.append([m])

#   print(masses)
   
  # spectrumCounter = counter(spectrum)
  # createList(l1, masses, spectrumCounter)
   print(l1)
   
   leader = []
   leadscore = 0

   while len( l1 ) != 0 :
      l1 = expandList2(l1, masses)
      print( len(l1), ' ', len(l1[0]) )

      scores = getScores(l1, spectrum)
      
  #    print(scores)
      for i in range(0,len(l1)):
         mlist = l1[i]
         
         if scores[i] > leadscore:
            leader = list(mlist)
            leadscore = scores[i] 
              
      l1 = Cut(l1, scores, spectrum, N)

   outputList(leader)   
 
      
###############################################################



def readSpectrum(fileIn):
   fin = open(fileIn,"r")
   spec = []
   lines = fin.readlines()
   
   for lns in lines:
      wds = lns.split(' ')
      for k in wds:  
        spec.append(int(k.strip())) 
   return spec
   
   
   
##############################################################   
spectrum = readSpectrum("input.dat")
#print(spectrum) 
masses = getMasses()

#massList = [ 1, 10, 100 ]
#print(getSpectrumByMass(massList))

LeaderBoardCyclopeptideSequencing(spectrum)
#aa = []
#createList(aa,  masses)
#print(aa)
#aa = expandList(aa, masses)
#print(aa)  
#print(getLinearSpectrum([1,2,4,8]))

