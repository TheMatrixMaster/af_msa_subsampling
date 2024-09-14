#!/bin/bash
#SBATCH --job-name=esm_conformers
#SBATCH --output=logs/%x-%j.out
#SBATCH --partition=long
#SBATCH --time=23:59:00
#SBATCH --gpus=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8GB
#SBATCH --partition long

# Activate conda environment
module --force purge
conda init
conda activate esm

OUTDIR=/home/mila/s/stephen.lu/scratch/esm_conformers

# python inference.py \
#     --jobname apo \
#     --fasta /home/mila/s/stephen.lu/proteins/data/test_set/apo/apo.fasta \
#     --output_dir $OUTDIR \
#     --n 5

# python inference.py \
#     --jobname codnas \
#     --fasta /home/mila/s/stephen.lu/proteins/data/test_set/condas/codnas.fasta \
#     --output_dir $OUTDIR \
#     --n 5

# python inference.py \
#     --jobname ped_114 \
#     --fasta /home/mila/s/stephen.lu/proteins/data/test_set/ped_114/ped_114.fasta \
#     --output_dir $OUTDIR \
#     --n 10

# python inference.py \
#     --jobname bpti \
#     --fasta /home/mila/s/stephen.lu/proteins/data/test_set/bpti/bpti.fasta \
#     --output_dir $OUTDIR \
#     --n 100

python inference.py \
    --jobname atlas_test \
    --fasta /home/mila/s/stephen.lu/proteins/data/test_set/atlas_test/atlas_test.fasta \
    --output_dir $OUTDIR \
    --n 100