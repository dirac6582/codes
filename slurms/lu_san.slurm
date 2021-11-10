#!/bin/bash

#SBATCH -J JobName            # Job name
#SBATCH -o JobOutput.out      # Name of stdout output file (%j expands to jobId)
#SBATCH -N 1                  # Total number of nodes requested
#SBATCH -n 16                 # Total number of mpi tasks requested
#SBATCH -t 48:00:00           # Run time (hh:mm:ss) - 1.5 hours
#SBATCH -p sky6126            # partition name (node name)



# Assuming module load prun (as well as any mpi module e.g. impi)
module load oneapi/mpi

# unlimit the maximum number of the processors
ulimit -s unlimited



# output calculation settings
echo
echo    START DATE       : `date`
echo   SLURM_JOBID       : ${SLURM_JOBID}
echo SLURM_SUBMIT_DIR    : ${SLURM_SUBMIT_DIR}
echo SLURM_CPUS_PER_TASK : ${SLURM_CPUS_PER_TASK}
echo   SLURM_NTASKS      : ${SLURM_NTASKS}

#echo   PBS_NODENUM    : ${PBS_NODENUM}
#echo    PBS_O_HOST    : ${PBS_O_HOST}
#echo    PBS_SERVER    : ${PBS_SERVER}
#echo   PBS_O_QUEUE    : ${PBS_O_QUEUE}
#echo   PBS_ARRAYID    : ${PBS_ARRAYID}
#echo     PBS_QUEUE    : ${PBS_QUEUE}
#echo      used_nodes  : ${used_nodes}
#echo       num_nodes  : ${num_nodes}
#echo   proc_per_node  : ${proc_per_node}
#echo        num_proc  : ${num_proc}
echo     hostname     : `hostname`
echo


#
#######################  End of Initialization   ##############################
#

# move to working dir
cd $SLURM_SUBMIT_DIR


# write your commands here
mpirun -np 4 echo "test done"
