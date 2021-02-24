
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

n = 8

n_q = n
n_b = n

qc_output = QuantumCircuit(n_q, n_b)

for j in range(n):
    qc_output.measure(j,j)

qc_output.draw()


