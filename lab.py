from mpi4py import MPI
import numpy as np

# linear nodes code of adding 2 arrays
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

dest = (rank + 1) % size
src = (rank - 1) % size

x = [(1, 13, 15, 18)]
y = [(4, 8, 21, 30)]

res = [] * len(y)

if rank == 0:
    for i in range(size - 1):
        x_chunk = np.array_split(x, size - 1)
        y_chunk = np.array_split(y, size-1)
        print("I'm node {} sending to node {}".format(rank, i+1))
        comm.send(x_chunk, dest=i+1, tag=i+1)
        comm.send(y_chunk, dest=i+1, tag=i+1)

    for i in range(size-1):
        print("Got result appending: ")
        gett = comm.recv(source=i+1)
        res.append(gett)

else:
    print("Hello in {}".format(rank))
    x_chunk = comm.recv(source=0)
    y_chunk = comm.recv(source=0)
    add = np.array([0]*len(x_chunk))

    for i in range(x_chunk):
        add = x_chunk[i]+y_chunk[i]

    comm.send(add, dest=0)

print(res)
