#2019-90142 Hyun-Wook Park


#Samsung Electronics

import Stock_hmm
states = ('fall', 'stable','rise') #common stock state
symbols = ('1', '2', '3') #preferred stock trend



start_prob = { #초기 시작 확률
    'fall' : 0.35,
    'stable' : 0.47,
    'rise' : 0.18
}

trans_prob = { #State 사이의 P
    'fall': { 'fall' : 0.2, 'stable' : 0.6, 'rise' : 0.2},
    'stable': { 'fall' : 0.5, 'stable' : 0.38, 'rise' :0.13 },
    'rise': {'fall' : 0.33, 'stable' : 0.33, 'rise' :0.33}
}

emit_prob = { #Preferred - Common stock
    'fall': { '1' : 0.82, '2' : 0.17, '3' : 0.01  },
    'stable': { '1' : 0.25, '2' : 0.74, '3' : 0.01 },
    'rise': { '1' : 0.01, '2' : 0.01, '3' : 0.98 }
}

model = Stock_hmm.Model(states, symbols, start_prob, trans_prob, emit_prob)
sequence = ['2','2','2','1','1','1','3','1','2','2','1','1','3','3','2','2','1']
print(model.evaluate(sequence)) # Likelihood
print(model.decode(sequence)) # 최적상태열 추정



#Keyang Electric Machinery 

states = ('fall', 'stable','rise') #common stock state
symbols = ('1', '2', '3') #preferred stock trend



start_prob = { #초기 시작 확률
    'fall' : 0.35,
    'stable' : 0.53,
    'rise' : 0.12
}

trans_prob = { #State 사이의 P
    'fall': { 'fall' : 0.71, 'stable' : 0.14, 'rise' : 0.14},
    'stable': { 'fall' : 0.25, 'stable' : 0.25, 'rise' :0.50 },
    'rise': {'fall' : 0.60, 'stable' : 0.20, 'rise' :0.20}
}

emit_prob = { #Preferred - Common stock
    'fall': { '1' : 0.66, '2' : 0.01, '3' : 0.33  },
    'stable': { '1' : 0.33, '2' : 0.44, '3' : 0.22 },
    'rise': { '1' : 0.49, '2' : 0.02, '3' : 0.49 }
}

model = Stock_hmm.Model(states, symbols, start_prob, trans_prob, emit_prob)
sequence = ['3','2','2','2','3','1','3','1','1','2','3','3','1','1','1','1','1']
print(model.evaluate(sequence)) # Likelihood
print(model.decode(sequence)) # 최적상태열 추정







