#!/bin/bash 
#SBATCH --job-name=1n1n 
#SBATCH --account=NN9464K 
## Syntax is d-hh:mm:ss 
#SBATCH --time=0-05:00:00 
#SBATCH --nodes=4
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
echo "start running log_Ni67_gs8_tr_j1n_j1n.txt ..."
cat > Ni67_gs8_1n_1n.input <<EOF
&input
  fn_int   = "gs8.snt"
  fn_ptn_l = "Ni67_gs8_n.ptn"
  fn_ptn_r = "Ni67_gs8_n.ptn"
  fn_load_wave_l = "Ni67_gs8_j1n.wav"
  fn_load_wave_r = "Ni67_gs8_j1n.wav"
  hw_type = 2
  eff_charge = 1.5, 0.5
  gl = 1.0, 0.0
  gs = 4.189, -2.869
&end
EOF
mpiexec ./transit.exe Ni67_gs8_1n_1n.input > log_Ni67_gs8_tr_j1n_j1n.txt  

rm -f Ni67_gs8_1n_1n.input


