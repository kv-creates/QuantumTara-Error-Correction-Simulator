import numpy as np
from src.gates import H, X, ry
def test_h():
    assert np.allclose(H @ H, np.eye(2))
def test_ry():
    assert np.allclose(ry(0), np.eye(2))
