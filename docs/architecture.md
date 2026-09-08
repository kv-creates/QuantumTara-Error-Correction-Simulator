# Architecture

Statevector complex128. Gates as unitary matmul. Noise as Kraus sampling. VQE as COBYLA-like descent.

```mermaid
flowchart LR
  INIT[|0>] --> U[Unitary] --> N[Noise] --> M[Measure] --> EC[Correct] --> VQE[Optimize]
```
