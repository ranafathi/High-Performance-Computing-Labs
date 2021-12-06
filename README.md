# High-Performance-Computing-Labs
Codes from CSE415:  HPC university course for Fall 2021, FOE ASU CHEP
<br/>
### lab.py  
 First code written for P2P communication deliverable  
 **Requested:** A mpi4py code that has 3 processors (master node and 2 executing nodes) that add 2 arrays and return result in new array.  
 
 To run lab.py, in terminal type:  
 `mpiexec -np 3 python lab.py`

### ring.py  
 **Requested:** A mpi4py code that has a ring-shape of processors that divides 2 arrays on the amount of processors and returns their sum in the original (master) node.
 
 To run ring.py, in terminal type:  
 `mpiexec -np (number of processors in ring) python ring.py`
