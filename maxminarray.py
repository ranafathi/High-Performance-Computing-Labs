from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

x = [1, 2, 4, 6, 7, 3, 5]
p1_chunk = []
p2_chunk = []
res = []
i = 0

if rank == 0:

    y = int(len(x) / 2)

    while i < len(x) / 2:
        p1_chunk.append(x[i])
        i += 1

    while y < len(x):
        p2_chunk.append(x[y])
        y += 1

    print(p1_chunk, p2_chunk)

    comm.send(p1_chunk, dest=1, tag=1)
    comm.send(p2_chunk, dest=2, tag=2)

    x = comm.recv(source=1)
    x += comm.recv(source=2)

    res = [np.min(x), np.max(x)]
    print(res)

elif rank == 1:

    var = comm.recv(source=0)
    max_element = np.max(var)
    min_element = np.min(var)
    new_arr = [min_element, max_element]
    print(new_arr)
    comm.send(new_arr, dest=0)

elif rank == 2:

    var = comm.recv(source=0)
    max_element = np.max(var)
    min_element = np.min(var)
    new_arr = [min_element, max_element]
    print(new_arr)
    comm.send(new_arr, dest=0)
