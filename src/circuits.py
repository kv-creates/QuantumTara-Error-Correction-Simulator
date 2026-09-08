import numpy as np
from .gates import H, X, apply

def zero_state(n):
    s=np.zeros(2**n,complex); s[0]=1; return s

def bell_state():
    s=zero_state(2)
    s=apply(s,H,[0],2)
    s=apply(s,None,[0,1],2)  # CNOT path uses gate=None
    return s

def counts(state, shots=1024):
    probs=np.abs(state)**2
    probs/=probs.sum()
    # deterministic mock: round
    n=len(state)
    return {format(i,f'0{int(np.log2(n))}b'):round(float(p)*shots) for i,p in enumerate(probs)}

def teleport_fidelity(noise_p=0.0):
    # ideal 1.0, linear drop
    return round(max(0,1-noise_p*1.5),3)
