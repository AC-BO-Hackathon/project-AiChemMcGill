**Authors**: Ben Weiser, Jérôme Genzling, Nicolas Gastellu, and Sylvester Zhang


# Intro

We built a tool which optimizes a protein to achieve better binding affinity to a certain substrate. This can have applications to biologics such as antibody therapeutics, enzymology, and in the case of this project, biosensors. We aimed to use Bayesian optimization to mutate the residues of a protein to achieve better binding affinity to fentanyl. This can be used for drug testing to detect fentanyl at higher sensitivities. 


# Protein-ligand system of interest

As a proof of concept, we focused on a polypeptide which was computationally designed to have a high binding affinity to the opiate fentanyl (see References section). Our code improves upon this peptide using the method described below.


# Methods

Our methodology was to use a pre-train a BERT language model trained to predict binding of ligands to a given protein from a sequence publish by Andrew E Blanchard. We give the amino acid sequence of the protein and the SMILES string of fentanyl to this model and it outputs score related to binding affinity. We then use Bayesian optimization to query position and amino acid to mutate to and subsequently predict the next best position and amino acid to try next. We want to start with a protein that already has affinity to fentanyl so we took a previously developed protein published by Lisa M. Eubanks. We analyzed the protein and selected the residues with 5 angstroms of the ligand to be selected for possible sites of mutagenesis. Then take a mutation if we find it increased the binding above a certain threshold, and do this until we find 3 mutations chosen by BO which our language model predicts to have high binding affinity. We compared the methodology to two baselines: (i) random mutations and (ii) a rudimentary genetic algorithm.

# What you'll find in this repository

* `final_notebook.ipynb`: This Jupyter notebook contains most of code we developped for this project. It also includes our tests on our protein-ligand system of interest and the comparison of our results with the aforementioned benchmarks. It is our pride and joy. We ran it on Google Colab, so you should be able to copy it and run it yourself, just make sure to uncomment the code in the first cell which installs all of the dependencies.
* `get_close_resids.py`: A helper module which we wrote to identify the protein residues which are within some distance `rcut` (which we set to 5Å) to the ligand.
* `5tzo.pdb`: A PDB file containing the protein-ligand structure of our system of interest. (Obtained from [here](https://www.rcsb.org/structure/5TZO)).
* `requirements.txt`: The list of our code's dependencies. It is not necessary if you plan on running `final_notebook.ipynb` directly on Google Colab.


# References

* Starting protein found [here](https://www.rcsb.org/structure/5TZO). ([Relevant paper](https://doi.org/10.7554/eLife.28909))  

* Binding affinity model we used: https://github.com/ORNL/affinity_pred/tree/master ([Relevant paper](https://doi.org/10.1177/10943420221121804))

Thanks for checking our project out! 
