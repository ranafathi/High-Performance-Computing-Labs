from mpi4py import MPI
from scipy import misc
import numpy as np
import cv2 as cv
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()

if rank==0:
    img=misc.face()
    height=img.shape[0]
    width=img.shape[1]

    chunks=np.array_split(img,size-1,0)

    for s_index in range(0,size-1):
        comm.send(chunks[s_index],dest=s_index+1)

else:
    chunk=comm.recv(source=0)
    cv.imwrite('newdace_node_{}.png'.format(rank),chunk)