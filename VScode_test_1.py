
#import pandas as pd
import numpy as np
import json
import random
import dimod
from dwave.system import LeapHybridSampler
from dwave.system import DWaveSampler, EmbeddingComposite

import numpy as np
from timeit import default_timer as timer
start = timer()

print('hello   ')

n = 50
fsel = 1
fhss = 1
#
print('n = ', n)


# Initialize Q matrix
Q = {}

# Initialize Q [n,n] to zero

for j in range(n):
    for k in range(n):
        #
        Q[(j,k)] = 0.0

# Qubo n=50 case: F = 2098
print('fsel = ', fsel)
#
if(fsel==1):
    Q[(0,3)]=-39
    Q[(0,42)]=72
    Q[(0,43)]=99
    Q[(0,48)]=57
    Q[(1,6)]=-78
    Q[(1,13)]=28
    Q[(1,31)]=-15
    Q[(2,10)]=84
    Q[(2,43)]=-86
    Q[(3,0)]=-39
    Q[(3,10)]=77
    Q[(3,21)]=-43
    Q[(3,26)]=12
    Q[(3,37)]=86
    Q[(3,38)]=81
    Q[(3,48)]=48
    Q[(4,8)]=51
    Q[(4,15)]=75
    Q[(4,19)]=53
    Q[(5,6)]=-2
    Q[(5,13)]=68
    Q[(5,14)]=3
    Q[(5,15)]=66
    Q[(5,20)]=-89
    Q[(5,23)]=90
    Q[(5,30)]=76
    Q[(6,1)]=-78
    Q[(6,5)]=-2
    Q[(6,16)]=97
    Q[(6,17)]=65
    Q[(6,31)]=50
    Q[(6,47)]=-2
    Q[(6,49)]=22
    Q[(7,41)]=91
    Q[(7,48)]=19
    Q[(8,4)]=51
    Q[(8,28)]=22
    Q[(8,30)]=7
    Q[(8,44)]=-22
    Q[(8,47)]=10
    Q[(9,19)]=77
    Q[(9,29)]=-42
    Q[(9,40)]=-40
    Q[(10,2)]=84
    Q[(10,3)]=77
    Q[(10,17)]=-35
    Q[(10,40)]=86
    Q[(10,41)]=62
    Q[(10,46)]=-75
    Q[(11,19)]=-94
    Q[(11,24)]=95
    Q[(11,45)]=-25
    Q[(11,46)]=-25
    Q[(12,29)]=14
    Q[(12,39)]=-45
    Q[(12,42)]=-48
    Q[(12,46)]=25
    Q[(13,1)]=28
    Q[(13,5)]=68
    Q[(13,18)]=24
    Q[(13,22)]=31
    Q[(13,29)]=78
    Q[(13,35)]=-59
    Q[(14,5)]=3
    Q[(14,18)]=72
    Q[(14,20)]=-45
    Q[(14,25)]=38
    Q[(14,26)]=-55
    Q[(14,35)]=53
    Q[(15,4)]=75
    Q[(15,5)]=66
    Q[(15,34)]=-40
    Q[(15,36)]=55
    Q[(16,6)]=97
    Q[(16,19)]=78
    Q[(16,22)]=65
    Q[(16,23)]=16
    Q[(16,24)]=-30
    Q[(17,6)]=65
    Q[(17,10)]=-35
    Q[(17,32)]=49
    Q[(18,13)]=24
    Q[(18,14)]=72
    Q[(18,18)]=-99
    Q[(18,21)]=60
    Q[(18,47)]=-78
    Q[(19,4)]=53
    Q[(19,9)]=77
    Q[(19,11)]=-94
    Q[(19,16)]=78
    Q[(20,5)]=-89
    Q[(20,14)]=-45
    Q[(20,30)]=28
    Q[(20,37)]=-17
    Q[(21,3)]=-43
    Q[(21,18)]=60
    Q[(21,24)]=43
    Q[(21,28)]=-70
    Q[(21,34)]=-98
    Q[(21,45)]=-81
    Q[(21,49)]=87
    Q[(22,13)]=31
    Q[(22,16)]=65
    Q[(22,26)]=-70
    Q[(22,33)]=10
    Q[(22,42)]=43
    Q[(22,47)]=90
    Q[(23,5)]=90
    Q[(23,16)]=16
    Q[(23,32)]=9
    Q[(23,35)]=-31
    Q[(24,11)]=95
    Q[(24,16)]=-30
    Q[(24,21)]=43
    Q[(24,47)]=24
    Q[(25,14)]=38
    Q[(25,38)]=50
    Q[(26,3)]=12
    Q[(26,14)]=-55
    Q[(26,22)]=-70
    Q[(26,46)]=-3
    Q[(26,48)]=-65
    Q[(27,38)]=84
    Q[(27,43)]=-12
    Q[(28,8)]=22
    Q[(28,21)]=-70
    Q[(28,33)]=-62
    Q[(28,38)]=91
    Q[(28,49)]=-23
    Q[(29,9)]=-42
    Q[(29,12)]=14
    Q[(29,13)]=78
    Q[(29,49)]=-98
    Q[(30,5)]=76
    Q[(30,8)]=7
    Q[(30,20)]=28
    Q[(30,32)]=-12
    Q[(30,34)]=-14
    Q[(31,1)]=-15
    Q[(31,6)]=50
    Q[(31,34)]=48
    Q[(31,47)]=49
    Q[(32,17)]=49
    Q[(32,23)]=9
    Q[(32,30)]=-12
    Q[(33,22)]=10
    Q[(33,28)]=-62
    Q[(33,38)]=-66
    Q[(34,15)]=-40
    Q[(34,21)]=-98
    Q[(34,30)]=-14
    Q[(34,31)]=48
    Q[(34,39)]=18
    Q[(35,13)]=-59
    Q[(35,14)]=53
    Q[(35,23)]=-31
    Q[(35,40)]=88
    Q[(36,15)]=55
    Q[(36,40)]=77
    Q[(36,49)]=-44
    Q[(37,3)]=86
    Q[(37,20)]=-17
    Q[(37,47)]=71
    Q[(38,3)]=81
    Q[(38,25)]=50
    Q[(38,27)]=84
    Q[(38,28)]=91
    Q[(38,33)]=-66
    Q[(38,46)]=-9
    Q[(38,49)]=36
    Q[(39,12)]=-45
    Q[(39,34)]=18
    Q[(39,39)]=48
    Q[(39,42)]=67
    Q[(40,9)]=-40
    Q[(40,10)]=86
    Q[(40,35)]=88
    Q[(40,36)]=77
    Q[(41,7)]=91
    Q[(41,10)]=62
    Q[(41,44)]=64
    Q[(42,0)]=72
    Q[(42,12)]=-48
    Q[(42,22)]=43
    Q[(42,39)]=67
    Q[(43,0)]=99
    Q[(43,2)]=-86
    Q[(43,27)]=-12
    Q[(43,43)]=-58
    Q[(44,8)]=-22
    Q[(44,41)]=64
    Q[(45,11)]=-25
    Q[(45,21)]=-81
    Q[(45,47)]=12
    Q[(46,10)]=-75
    Q[(46,11)]=-25
    Q[(46,12)]=25
    Q[(46,26)]=-3
    Q[(46,38)]=-9
    Q[(46,47)]=-35
    Q[(47,6)]=-2
    Q[(47,8)]=10
    Q[(47,18)]=-78
    Q[(47,22)]=90
    Q[(47,24)]=24
    Q[(47,31)]=49
    Q[(47,37)]=71
    Q[(47,45)]=12
    Q[(47,46)]=-35
    Q[(48,0)]=57
    Q[(48,3)]=48
    Q[(48,7)]=19
    Q[(48,26)]=-65
    Q[(49,6)]=22
    Q[(49,21)]=87
    Q[(49,28)]=-23
    Q[(49,29)]=-98
    Q[(49,36)]=-44
    Q[(49,38)]=36


if(fhss==1):
    print('run HYB')
    sampler = LeapHybridSampler(solver={'category': 'hybrid'})
    sampleset = sampler.sample_qubo(Q, time_limit=30)
#
sampleset.info
print(sampleset)
#
sampleset.record.sample 
#
print(sampleset.lowest())
#
for sample in sampleset.samples():   
    print(sample)
#
Psol = sampleset.to_pandas_dataframe()    
print(Psol)
#
m = len(Psol)
for j in range(n):
    print(Psol[j])

s = json.dumps(sampleset.to_serializable())
print(s)

end = timer()
etime = end - start   # Time in secs
print('elapsed time (secs): ', etime)

