#!/bin/bash 
#SBATCH --job-name=13p13p 
#SBATCH --account=NN9464K 
## Syntax is d-hh:mm:ss 
#SBATCH --time=0-02:00:00
#SBATCH --nodes=32
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
echo "start running log_Ni67_gs8_tr_j13p_j13p.txt ..."
cat > Ni67_gs8_13p_13p.input <<EOF
&input
  fn_int   = "gs8.snt"
  fn_ptn_l = "Ni67_gs8_p.ptn"
  fn_ptn_r = "Ni67_gs8_p.ptn"
  fn_load_wave_l = "Ni67_gs8_j13p.wav"
  fn_load_wave_r = "Ni67_gs8_j13p.wav"
  hw_type = 2
  eff_charge = 1.5, 0.5
  gl = 1.0, 0.0
  gs = 4.189, -2.869
&end
EOF
mpiexec ./transit.exe Ni67_gs8_13p_13p.input > log_Ni67_gs8_tr_j13p_j13p.txt  

rm -f Ni67_gs8_13p_13p.input


