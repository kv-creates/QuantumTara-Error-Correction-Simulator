import numpy as np

def depolarizing(state, p=0.01):
    # mix with maximally mixed
    n=len(state)
    rho=np.outer(state,state.conj())
    rho=(1-p)*rho + p*np.eye(n)/n
    # return diagonal probs
    return np.real(np.diag(rho))

def readout_flip(counts_dict, q=0.02):
    out={}
    for k,v in counts_dict.items():
        # flip last bit with prob q mock
        out[k]=int(v*(1-q))
        fk=k[:-1]+('1' if k[-1]=='0' else '0')
        out[fk]=out.get(fk,0)+int(v*q)
    return out

def logical_gain(p):
    # 3-qubit code: logical error ~3p^2
    return round(3*p*p,5)
