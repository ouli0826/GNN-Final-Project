"""
functions to generate causal bayesian networks
"""
import numpy as np

def generate_dag(num_nodes, probability):
    """
    Generate a directed acyclic graph (DAG) with a given number of nodes and a given probability of
    an edge between two nodes. This is done by using the G(p, n) Erdős-Rényi model on a lower
    triangular matrix and then permuting the nodes. This is also done in the paper.
    Expected value of the number of edges: n * (n - 1) / 2 * p
    Returns an adjacency matrix representing the DAG.
    """
    # initialize the adjacency matrix
    DAG = np.zeros((num_nodes, num_nodes))
    # for every edge in the lower triangular matrix
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            # if the random number is less than the probability, add an edge between the nodes
            if np.random.rand() < probability:
                DAG[i, j] = 1
    # permute the nodes
    permutation = np.random.permutation(num_nodes)
    DAG = DAG[permutation, :]
    DAG = DAG[:, permutation]
    return DAG

