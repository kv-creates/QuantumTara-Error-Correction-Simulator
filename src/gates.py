import numpy as np
H=np.array([[1,1],[1,-1]],complex)/np.sqrt(2)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.array([[1,0],[0,-1]],complex)
I=np.eye(2,dtype=complex)

def ry(theta):
    return np.array([[np.cos(theta/2),-np.sin(theta/2)],[np.sin(theta/2),np.cos(theta/2)]],complex)

def kron(*mats):
    r=mats[0]
    for m in mats[1:]:
        r=np.kron(r,m)
    return r

def apply(state, gate, targets, n):
    # targets: list, only 1-qubit or CNOT 2-qubit supported
    if len(targets)==1:
        ops=[gate if i==targets[0] else I for i in range(n)]
        U=kron(*reversed(ops)) if n>1 else gate
        return U @ state
    if len(targets)==2:
        # CNOT control, target, only n=2 supported
        c,t=targets
        CNOT=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],complex)
        if (c,t)==(0,1):
            return CNOT @ state
        # swap trick for (1,0)
        SWAP=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]],complex)
        return SWAP @ CNOT @ SWAP @ state
    raise ValueError('unsupported')
