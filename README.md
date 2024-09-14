# MSA Subsampling with AlphaFold

Cloned from https://github.com/delalamo/af2_conformations and modified for easier usage on Mila SLURM cluster.

## Usage
First, setup the general conda environment:
```bash
# Create new conda environment
conda create -n af2_msa python=3.10
conda activate af2_msa

# Install hh-suite
conda install -c conda-forge -c bioconda hhsuite 
```

Next, clone alphafold repository and install the source code
```bash
git clone https://github.com/google-deepmind/alphafold
cd alphafold
pip install -e .
cd ..
```

Finally, clone this repository and install the required packages, alongside the alphafold params in the `/params` directory.
```bash
git clone https://github.com/TheMatrixMaster/af_msa_subsampling
cd af_msa_subsampling

# Download AlphaFold parameters
mkdir params
cd params
wget https://storage.googleapis.com/alphafold/alphafold_params_2022-12-06.tar
tar -xvf alphafold_params_2022-12-06.tar

# Install repo requirements
pip install -r requirements.txt
```

To run the script, use the following command:
```bash
python inference.py \
    --jobname <job_name> \
    --fasta <path_to_fasta_file> \
    --output_dir <output_directory> \
    --n <number_of_conformers_per_sequence> \
```
