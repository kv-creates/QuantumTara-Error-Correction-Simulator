from src.vqe import vqe_loop
def test_vqe():
    r=vqe_loop(5)
    assert r["best_energy"]<-1.0
