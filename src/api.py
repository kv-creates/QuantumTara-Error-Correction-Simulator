from fastapi import FastAPI
from .circuits import bell_state, counts, teleport_fidelity
from .vqe import vqe_loop
app=FastAPI(title="QuantumTara")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/run-circuit")
def r(body: dict):
    s=bell_state()
    return {"counts":counts(s,body.get("shots",1024)),"teleport":teleport_fidelity(body.get("noise",0.0))}
@app.post("/vqe")
def v(body: dict): return vqe_loop(body.get("steps",20))
@app.get("/visual-data")
def vd():
    s=bell_state()
    return {"counts":counts(s),"vqe":vqe_loop(15)}
