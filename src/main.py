from .circuits import bell_state, counts
from .vqe import vqe_loop
def demo():
    print(counts(bell_state()))
    print(vqe_loop(5)["best_energy"])
if __name__=="__main__": demo()
