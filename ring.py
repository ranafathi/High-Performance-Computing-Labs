from mpi4py import MPI
import numpy as np

# linear nodes code of adding 2 arrays
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

target = (rank + 1) % size
src = (rank - 1) % size

x = [(1, 13, 15, 18, 4, 13, 34)]
y = [(4, 8, 21, 30, 5, 13, 56)]

x_chunks = np.array_split(x, size)
y_chunks = np.array_split(y, size)

add = [] * len(y)

x_part = x_chunks[0]
y_part = y_chunks[0]

res = []*len(y_part)

if rank==0:
    for i in range(x_part.size):
     ctr = x_part[i]+y_part[i]
     res.append(ctr)

    x_chunks = np.delete(x_chunks, 0, 0)
    y_chunks = np.delete(y_chunks, 0, 0)

    comm.send(x_chunks, dest=target)
    comm.send(y_chunks, dest=target)
    comm.send(res, dest=target)

    x1 = comm.recv(source=src)
    y1 = comm.recv(source=src)
    add = comm.recv(source=src)

    print("result:" + str(add))

else:

    x_chunks = comm.recv(source=src)
    y_chunks = comm.recv(source=src)
    prev_res = comm.recv(source=src)

    x_part = x_chunks[0]
    y_part = y_chunks[0]

    res = []*len(y_chunks)
    for i in range(x_part.size):
        ctr = x_part[i]+y_part[i]
        res.append(ctr)

    prev_res+=res

    x_chunks = np.delete(x_chunks, 0, 0)
    y_chunks = np.delete(y_chunks, 0, 0)

    comm.send(x_chunks, dest= target)
    comm.send(y_chunks, dest=target)
    comm.send(prev_res, dest=target)