#!/bin/bash 
#SBATCH --qos=devel
#SBATCH --job-name=17n 
#SBATCH --account=NN9464K 
## Syntax is d-hh:mm:ss 
#SBATCH --time=0-01:00:00 
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8 
#SBATCH --cpus-per-task=16 
#SBATCH --mail-type=ALL 
#SBATCH --mail-user=jonkd@uio.no 
module --quiet purge  
module load intel/2020b 
module load Python/3.8.6-GCCcore-10.2.0 
set -o errexit  
set -o nounset 
export OMP_NUM_THREADS=32 
echo "start running log_Ni67_gs8_j17n.txt ..."
cat > Ni67_gs8_17n.input <<EOF
&input
  beta_cm = 10.0
  eff_charge = 1.5, 0.5, 
  fn_int = "gs8.snt"
  fn_ptn = "Ni67_gs8_n.ptn"
  fn_save_wave = "Ni67_gs8_j17n.wav"
  gl = 1.0, 0.0, 
  gs = 4.189, -2.869, 
  hw_type = 2
  is_double_j = .true.
  max_lanc_vec = 1000
  maxiter = 300
  mode_lv_hdd = 0
  mtot = 17
  n_block = 8
  n_eigen = 200
  n_restart_vec = 300
&end
EOF
mpiexec ./kshell.exe Ni67_gs8_17n.input > log_Ni67_gs8_j17n.txt  

rm -f tmp_snapshot_Ni67_gs8_n.ptn_17_* tmp_lv_Ni67_gs8_n.ptn_17_* Ni67_gs8_17n.input 


