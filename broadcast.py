from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = None

if rank == 0:
    data = [1,2,3,4,5,6,7,8,9,10]

bcast_data = comm.bcast(data, root=0)
print("Data = {0} from process {1}".format(bcast_data, rank))