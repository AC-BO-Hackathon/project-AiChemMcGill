#!/usr/bin/env python

import numpy as np
from scipy.spatial import KDTree
import MDAnalysis as mda

def binding_resids(pdb_path, ligand_resname, rcut):

    all_atoms = mda.Universe(pdb_path)

    ligand_resname = '7V7'


    ligand = all_atoms.select_atoms(f'resname {ligand_resname}')
    protein = all_atoms.select_atoms('protein')

    pr_tree = KDTree(protein.positions)
    li_tree = KDTree(ligand.positions)

    rcut = 5.0

    binding_inds = np.unique(np.hstack(li_tree.query_ball_tree(pr_tree,rcut))).astype('int')
    binding_resids = np.unique(protein[binding_inds].resids)
    return binding_resids

if __name__ == "__main__":

    pdbfile = "5tzo.pdb"
    ligand_resname = '7V7'
    rcut = 5.0 #in angstroms

    close_resids = binding_resids(pdbfile,ligand_resname,rcut)

    print(','.join([str(i) for i in close_resids]))
    print(f'\n{len(close_resids)}')


