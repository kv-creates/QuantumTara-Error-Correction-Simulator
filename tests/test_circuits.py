from src.circuits import bell_state, counts
def test_bell():
    s=bell_state()
    assert abs(abs(s[0])-0.707)<0.01
def test_counts():
    assert sum(counts(bell_state(),100).values())==100
