#!/bin/bash
#SBATCH -J phi4_test          # Job name
#SBATCH -o JobOutput_%j.out    # Name of stdout output file (%j expands to jobId)
#SBATCH -N 4                   # Total number of nodes requested
#SBATCH -n 512                  # Total number of mpi tasks requested
#SBATCH -p F4cpu               # partition name (node name) sky6126 F4cpu i8cpu
#SBATCH --mail-type=all        #※type はBEGIN, END, FAIL, REQUEUE, ALL のいずれか
#SBATCH --mail-user=tragic44cg@icloud.com  #メールアドレス指定

# tanryo_test2でborn effective chargeの計算を行う．


# Assuming module load prun (as well as any mpi module e.g. impi)
module load oneapi/compiler
module load oneapi/mkl
module load oneapi/mpi


# unlimit the maximum number of the processors
ulimit -s unlimited



# output calculation settings
echo
echo    START DATE       : `date`
echo   SLURM_JOBID       : ${SLURM_JOBID}
echo SLURM_SUBMIT_DIR    : ${SLURM_SUBMIT_DIR}
echo SLURM_CPUS_PER_TASK : ${SLURM_CPUS_PER_TASK}
echo SLURM_JOB_NUM_NODES : ${SLURM_JOB_NUM_NODES} # num of nodes allocated to the job
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

# qe environmental variables
 . /home/issp/materiapps/intel/espresso/espressovars.sh


MKL_DEBUG_CPU_TYPE=5
ulimit -s unlimited


# standard version



# gamma-point only
# srun /home/issp/vasp/vasp5/vasp.5.4.4.pl2/bin/vasp_gam > stdout.log 2>&1

# noncollinear
# srun /home/issp/vasp/vasp5/vasp.5.4.4.pl2/bin/vasp_ncl > stdout.log 2>&1
 

# dependent files dir
#DEPENDENT_DIR=/home/amano/sample

# set the needed environment variables
# . $DEPENDENT_DIR/environment_variables2
echo
echo "environment setting done"
echo 


# check if pw and pseudo directories exist
# . $DEPENDENT_DIR/check_directory.sh
echo
echo "check directory done"
echo 





###########################

#
#
# for i in supercell


# standard version
echo "PSI_SCRATCH"
echo ${PSI_SCRATCH}

# Activate Anaconda work environment for OpenDrift
source ~/.bashrc
source ~/.bash_profile
conda activate phi4

module purge
psi4 -n 16 -i naphthalene_cc.in -o naphthalene_cc.out 2>&1
#srun -n 1 psi4 -i toluene_opt.in -o toluene_opt.out 2>&1


# slack notification
# echo JOBID::${SLURM_JOBID} prefix::${prefix} finished | $DEPENDENT_DIR/slack_send.sh


# finish
echo
echo "PROGRAM END"
echo    END DATE       : `date`
