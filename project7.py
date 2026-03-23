# import os

# # Define input and output files
# receptor_file = "receptor.pdbqt"
# ligand_file = "ligand.pdbqt"
# trajectory_file = "trajectory.xtc"
# topology_file = "topology.tpr"
# admet_input_file = "ligand.sdf"
# admet_output_file = "admet_results.txt"
#
# # Define Autodock Vina parameters
# vina_command = "vina"
# vina_config_file = "vina_config.txt"
# vina_output_file = "vina_results.txt"
# vina_num_modes = 10
#
# # Define GROMACS parameters
# gmx_command = "gmx"
# gmx_em_input_file = "em.mdp"
# gmx_md_input_file = "md.mdp"
# gmx_output_file = "gromacs_results.txt"
# gmx_equilibration_steps = 10000
# gmx_production_steps = 100000
#
# # Define ADMETlab parameters
# admetlab_command = "admetlab"
# admetlab_properties = "all"
#
# # Define Autodock Vina command
# vina_cmd = f"{vina_command} --config {vina_config_file} --receptor {receptor_file} --ligand {ligand_file} --out {vina_output_file} --num_modes {vina_num_modes}"
#
# # Define GROMACS commands
# gmx_em_cmd = f"{gmx_command} grompp -f {gmx_em_input_file} -c {ligand_file} -p {receptor_file} -o {topology_file}"
# gmx_em_cmd += f" && {gmx_command} mdrun -v -deffnm em -nt 1"
# gmx_md_cmd = f"{gmx_command} grompp -f {gmx_md_input_file} -c em.gro -p {receptor_file} -o {topology_file}"
# gmx_md_cmd += f" && {gmx_command} mdrun -v -deffnm md -nt 1"
# gmx_rmsd_cmd = f"{gmx_command} rms -s {receptor_file} -f {trajectory_file} -o rmsd.xvg"
# gmx_rmsf_cmd = f"{gmx_command} rmsf -s {receptor_file} -f {trajectory_file} -o rmsf.xvg"
#
# # Define ADMETlab command
# admetlab_cmd = f"{admetlab_command} predict -i {admet_input_file} -p {admetlab_properties} -o {admet_output_file}"
#
# # Run Autodock Vina
# os.system(vina_cmd)
#
# # Run GROMACS
# os.system(gmx_em_cmd)
# os.system(gmx_md_cmd)
# os.system(gmx_rmsd_cmd)
# os.system(gmx_rmsf_cmd)
#
# # Run ADMETlab
# os.system(admetlab_cmd)
