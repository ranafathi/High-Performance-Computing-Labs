from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = None

if rank == 0:
    data = [[1, 2], [3, 4], [5, 6]]

scat = comm.scatter(data, root=0)
#print("Data {0} is at process {1}".format(scat, rank))

gath = comm.gather(scat,root=0)

if rank == 0:
    print("Data at process {0} is {1}".format(rank, gath))