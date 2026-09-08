import math

def h2_energy(theta):
    # mock H2 curve: min -1.137 at 0.5
    return -1.0 -0.137*math.exp(-((theta-0.5)**2)/0.2) + 0.05*theta

def vqe_loop(steps=20):
    theta=0.0; best=(theta,h2_energy(theta)); hist=[]
    lr=0.2
    for i in range(steps):
        e=h2_energy(theta)
        hist.append({"step":i,"theta":round(theta,3),"energy":round(e,4)})
        if e<best[1]: best=(theta,e)
        # numeric grad
        g=(h2_energy(theta+1e-3)-e)/1e-3
        theta-=lr*g
    return {"best_theta":round(best[0],3),"best_energy":round(best[1],4),"history":hist}
