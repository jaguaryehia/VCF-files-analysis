# import numpy as np
# import matplotlib.pyplot as plt
# from Bio.PDB import PDBParser
#
# def calculate_rmsd(coords1, coords2):
#     """Calculate the Root Mean Square Deviation (RMSD) between two sets of coordinates."""
#     diff = coords1 - coords2
#     rmsd = np.sqrt(np.mean(np.sum(diff ** 2, axis=1)))
#     return rmsd
#
# def calculate_rmsf(coords):
#     """Calculate the Root Mean Square Fluctuation (RMSF) for each atom in a set of coordinates."""
#     mean_coords = np.mean(coords, axis=0)
#     diff = coords - mean_coords
#     rmsf = np.sqrt(np.mean(np.sum(diff ** 2, axis=1)))
#     return rmsf
#
# # Load the initial structure from a PDB file
# parser = PDBParser()
# structure = parser.get_structure('protein', '6lu7.pdb')
#
# # Extract the coordinates of all atoms in the initial structure
# coords_ref = []
# for model in structure:
#     for chain in model:
#         for residue in chain:
#             for atom in residue:
#                 coords_ref.append(atom.get_coord())
# coords_ref = np.array(coords_ref)
#
# # Perform molecular dynamics simulation (you can replace this with your own MD code)
# # In this example, we're simply generating random fluctuations around the initial structure
# num_frames = 1000
# coords_traj = np.zeros((num_frames, coords_ref.shape[0], 3))
# for i in range(num_frames):
#     coords_traj[i] = coords_ref + np.random.normal(0, 0.1, coords_ref.shape)
#
# # Calculate RMSD and RMSF
# rmsd_values = []
# rmsf_values = []
# for coords in coords_traj:
#     rmsd = calculate_rmsd(coords_ref, coords)
#     rmsf = calculate_rmsf(coords)
#     rmsd_values.append(rmsd)
#     rmsf_values.append(rmsf)
#
# # Plot RMSD
# plt.figure(figsize=(8, 6))
# plt.plot(rmsd_values)
# plt.xlabel('Frame')
# plt.ylabel('RMSD (Å)')
# plt.title('RMSD during MD Simulation')
# plt.grid(True)
# plt.show()
#
# # Plot RMSF
# plt.figure(figsize=(8, 6))
# plt.plot(rmsf_values)
# plt.xlabel('Atom')
# plt.ylabel('RMSF (Å)')
# plt.title('RMSF during MD Simulation')
# plt.grid(True)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from Bio.PDB import PDBParser
#
# def calculate_rmsd(coords1, coords2):
#     """Calculate the Root Mean Square Deviation (RMSD) between two sets of coordinates."""
#     diff = coords1 - coords2
#     rmsd = np.sqrt(np.mean(np.sum(diff ** 2, axis=1)))
#     return rmsd
#
# def calculate_rmsf(coords):
#     """Calculate the Root Mean Square Fluctuation (RMSF) for each atom in a set of coordinates."""
#     mean_coords = np.mean(coords, axis=0)
#     diff = coords - mean_coords
#     rmsf = np.sqrt(np.mean(np.sum(diff ** 2, axis=1)))
#     return rmsf
#
# # Load the initial structure from a PDB file
# parser = PDBParser()
# structure = parser.get_structure('protein', 'pddbb/complexCID.pdb')
#
# # Extract the coordinates of all atoms in the initial structure
# coords_ref = []
# for model in structure:
#     for chain in model:
#         for residue in chain:
#             for atom in residue:
#                 coords_ref.append(atom.get_coord())
# coords_ref = np.array(coords_ref)
#
# # Perform molecular dynamics simulation (you can replace this with your own MD code)
# # In this example, we're simply generating random fluctuations around the initial structure
# simulation_time = 1.0  # Simulation time in microseconds (1000 nanoseconds)
# time_step_ns = 0.01   # Time step in nanoseconds
# num_frames = int(simulation_time / (time_step_ns ))
# coords_traj = np.zeros((num_frames, coords_ref.shape[0], 3))
# for i in range(num_frames):
#     coords_traj[i] = coords_ref + np.random.normal(0, 0.1, coords_ref.shape)
#
# # Calculate RMSD and RMSF
# rmsd_values = []
# rmsf_values = []
# time_values = []
# for i, coords in enumerate(coords_traj):
#     time = (i + 1) * time_step_ns * 1000
#     rmsd = calculate_rmsd(coords_ref, coords)
#     rmsf = calculate_rmsf(coords)
#     rmsd_values.append(rmsd)
#     rmsf_values.append(rmsf)
#     time_values.append(time)
#
# # Plot RMSD
# plt.figure(figsize=(8, 6))
# plt.plot(time_values, rmsd_values)
# plt.xlabel('Time (ns)')
# plt.ylabel('RMSD (Å)')
# plt.title('RMSD during MD Simulation')
# plt.grid(True)
# plt.show()
#
# # Plot RMSF
# plt.figure(figsize=(8, 6))
# plt.plot(rmsf_values)
# plt.xlabel('Atom')
# plt.ylabel('RMSF (Å)')
# plt.title('RMSF during MD Simulation')
# plt.grid(True)
# plt.show()

import argparse
import numpy as np


# Define a simple force field implementation
class ForceField:
    def __init__(self, atom_types, bond_params, angle_params, lj_params):
        self.atom_types = atom_types
        self.bond_params = bond_params
        self.angle_params = angle_params
        self.lj_params = lj_params

    def compute_energy(self, coordinates):
        # Compute bonded energy
        bond_energy = self.compute_bond_energy(coordinates)
        angle_energy = self.compute_angle_energy(coordinates)

        # Compute non-bonded (Lennard-Jones) energy
        lj_energy = self.compute_lj_energy(coordinates)

        total_energy = bond_energy + angle_energy + lj_energy
        return total_energy

    def compute_bond_energy(self, coordinates):
        # Compute energy from bond interactions
        energy = 0.0
        for atom1, atom2 in self.bond_params:
            k, r0 = self.bond_params[(atom1, atom2)]
            atom1_coord = coordinates[atom1]
            atom2_coord = coordinates[atom2]
            bond_length = np.linalg.norm(atom1_coord - atom2_coord)
            bond_energy = 0.5 * k * (bond_length - r0) ** 2
            energy += bond_energy
        return energy

    def compute_angle_energy(self, coordinates):
        # Compute energy from angle interactions
        energy = 0.0
        for atom1, atom2, atom3 in self.angle_params:
            k, theta0 = self.angle_params[(atom1, atom2, atom3)]
            atom1_coord = coordinates[atom1]
            atom2_coord = coordinates[atom2]
            atom3_coord = coordinates[atom3]
            vector1 = atom1_coord - atom2_coord
            vector2 = atom3_coord - atom2_coord
            cos_theta = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
            angle_energy = 0.5 * k * (cos_theta - np.cos(theta0)) ** 2
            energy += angle_energy
        return energy

    def compute_lj_energy(self, coordinates):
        # Compute energy from Lennard-Jones interactions
        energy = 0.0
        for atom1, atom2 in self.lj_params:
            epsilon, sigma = self.lj_params[(atom1, atom2)]
            atom1_coord = coordinates[atom1]
            atom2_coord = coordinates[atom2]
            distance = np.linalg.norm(atom1_coord - atom2_coord)
            lj_energy = 4 * epsilon * ((sigma / distance) ** 12 - (sigma / distance) ** 6)
            energy += lj_energy
        return energy


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Molecular Dynamics Simulation')

    parser.add_argument('--pdb_file', type=str, required=True, help='Path to the PDB file')
    parser.add_argument('--simulation_time', type=float, default=10.0, help='Simulation time in nanoseconds')
    parser.add_argument('--time_step', type=float, default=0.1, help='Time step in picoseconds')
    parser.add_argument('--temperature', type=float, default=300.0, help='Temperature in Kelvin')

    args = parser.parse_args()
    return args


def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Access the parsed arguments
    pdb_file = args.pdb_file
    simulation_time = args.simulation_time
    time_step = args.time_step
    temperature = args.temperature

    # Print the values for verification
    print('PDB file:', pdb_file)
    print('Simulation time (ns):', simulation_time)
    print('Time step (ps):', time_step)
    print('Temperature (K):', temperature)

    # Define the force field parameters
    atom_types = ['C', 'N', 'O', 'H']
    bond_params = {('C', 'N'): (100.0, 1.2), ('N', 'O'): (120.0, 1.3)}  # Example bond parameters
    angle_params = {('C', 'N', 'O'): (50.0, np.pi / 3)}  # Example angle parameters
    lj_params = {('C', 'C'): (0.5, 1.0), ('N', 'O'): (1.0, 1.2)}  # Example LJ parameters

    # Create an instance of the force field
    force_field = ForceField(atom_types, bond_params, angle_params, lj_params)

    # Example usage: compute energy for a set of coordinates
    coordinates = np.random.rand(100, 3)  # Example coordinates
    energy = force_field.compute_energy(coordinates)
    print('Total energy:', energy)


if __name__ == '__main__':
    main()
