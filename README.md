# QuantumTara Error Correction Simulator (QuantumTara-Error-Correction-Simulator)

> Quantum science statevector simulator: 1-3 qubit gates, Bell teleportation, 3-qubit bit-flip code, depolarizing noise, VQE ground-state solver. No Qiskit needed.

![License](https://img.shields.io/badge/license-MIT-green) ![Python](https://img.shields.io/badge/python-3.11-blue) ![Quantum](https://img.shields.io/badge/quantum-statevector-purple) ![Visuals](https://img.shields.io/badge/visuals-heavy-orange)

## Overview
From Bloch sphere to logical qubits. Simulates ideal and noisy quantum circuits with heavy visuals for intuition.

## Problem Statement
Quantum error rates block useful computation. Students need open, visual, testable tools for gates, noise, correction, VQE without cloud access.

## Solution Architecture
```mermaid
graph TD
  A[Statevector |000>] --> B[Gates: H X CNOT Ry]
  B --> C[Noise: Depolarizing + Readout]
  C --> D[Correction: 3-qubit repetition]
  D --> E[VQE Loop: Ansatz + Optimizer]
  E --> F[Visuals: Bloch + Histogram + Energy]
```

## Visuals
Heavy visuals in `app/index.html`: Bloch sphere (Canvas), counts histogram (Chart.js), VQE energy convergence, circuit diagram (Mermaid).

![Bloch](https://via.placeholder.com/800x400/4b0082/ffffff?text=QuantumTara+Bloch+Sphere)
![Counts](https://via.placeholder.com/800x300/1f77b4/ffffff?text=Counts+Histogram)
![VQE](https://via.placeholder.com/800x300/d62728/ffffff?text=VQE+Energy+Convergence)

## Quick Start
```bash
git clone https://github.com/kv-creates/QuantumTara-Error-Correction-Simulator.git
cd QuantumTara-Error-Correction-Simulator
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
python -m src.main --demo
# open app/index.html for visuals
```

## API
```bash
GET /health
POST /run-circuit
POST /vqe
GET /visual-data
```

## Tests
```bash
pytest -q
```

## References
- Nielsen Chuang, Quantum Computation
- Qiskit Textbook
- Peruzzo VQE 2014

## License
MIT - kv-creates 2026
