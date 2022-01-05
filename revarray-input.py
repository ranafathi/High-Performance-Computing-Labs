from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

x = []
n = int(input("Number of array elements: "))

for i in range(0, n):
    elements = int(input())
    x.append(elements)

temp1 = []
temp2 = []
i = 0

if rank == 0:
    y = int(len(x) / 2)

    while i < len(x) / 2:
        temp1.append(x[i])
        i += 1

    while y < len(x):
        temp2.append(x[y])
        y += 1

    print(temp1, temp2)

    comm.send(temp1, dest=1)
    comm.send(temp2, dest=2)

    x = comm.recv(source=2)
    x += comm.recv(source=1)
    print(x)

elif rank == 1:
    var = comm.recv(source=0)
    var = var[::-1]
    print(var)
    comm.send(var, dest=0)

elif rank == 2:
    var = comm.recv(source=0)
    var = var[::-1]
    print(var)
    comm.send(var, dest=0)
