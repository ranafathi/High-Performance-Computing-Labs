# High-Performance-Computing-Labs
Codes from CSE415:  HPC university course for Fall 2021, FOE ASU CHEP
<br/>
### lab.py  
 First code written for P2P communication deliverable  
 **Requested:** A mpi4py code that has 3 processes (master node and 2 executing nodes) that add 2 arrays and return result in new array.  
 
 To run lab.py, in terminal type:  
 `mpiexec -np 3 python lab.py`

### ring.py  
 **Requested:** A mpi4py code that has a ring-shape of processes that divides 2 arrays on the amount of processes and returns their sum in the original (master) node.
 
 To run ring.py, in terminal type:  
 `mpiexec -np (number of processors in ring) python ring.py`

### reversearray.py  
 **Requested:** A mpi4py code that takes an array of integers, splits it into 2 processes and returns the array in reverse.
 
 To run reversearray.py, in terminal type:  
 `mpiexec -np 3 python reversearray.py`

### revarray-input.py  
 **Requested:** A mpi4py code that takes an input from the user as an array of integers, splits it into 2 processes and returns the array in reverse.
 
 To run revarray-input.py  , in terminal type:  
 `mpiexec -np 3 python reversearray.py`
