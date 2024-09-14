"""Generates n conformations for each sequence in a fasta file using AlphaFold MSA subsampling

Raises:
    FileNotFoundError: _description_
    ValueError: _description_
    
Usage:
    inference.py --jobname <jobname> --fasta <fasta> --output_dir <output_dir> [--n <n>] [--msa_depth <msa_depth>] [--af_model_id <af_model_id>]

Example:
    python inference.py --jobname "job1" --fasta "data/seqs.fasta" --output_dir "output"
"""

from scripts import predict
from scripts import mmseqs2
from argparse import ArgumentParser
from Bio import SeqIO
from timeit import default_timer as timer
import os

from absl import logging
logging.set_verbosity(logging.DEBUG)


def sample(jobname, seq, outdir, n=1, msa_depth=32, model_id=2):
    """Sample n conformations for a given sequence with MSA subsampling

    Args:
        jobname (_type_): _description_
        seq (_type_): _description_
        outname (_type_): _description_
        n (int, optional): _description_. Defaults to 1.
        msa_depth (int, optional): _description_. Defaults to 32.
        model_id (int, optional): _description_. Defaults to 2.
    """
    mmseqs2_runner = mmseqs2.MMSeqs2Runner(jobname, seq, outdir=outdir)
    a3m_lines, _ = mmseqs2_runner.run_job()

    for i in range(n):
        start = timer()
        outname = os.path.join(outdir, f"conformer-{i}.pdb")
        predict.predict_structure_no_templates(
            seq,
            outname,
            a3m_lines,
            model_id = model_id,
            max_msa_clusters = msa_depth // 2,
            max_extra_msa = msa_depth,
            max_recycles = 1
        )
        end = timer()
        print(f"Model {i} generated in {end-start:.2f} seconds")
        


def main():
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Read fasta file
    if not os.path.exists(args.fasta):
        raise FileNotFoundError(f"File not found: {args.fasta}")
    
    seqs = list(SeqIO.parse(args.fasta, "fasta"))
    
    if len(seqs) == 0:
        raise ValueError("No sequences found in fasta file")
    
    # Sample n conformations for each sequence
    for i, seq in enumerate(seqs):
        print(f"########## Processing {seq.id} ({i+1}/{len(seqs)}) ##########")
        outdir = os.path.join(args.output_dir, args.jobname, seq.id)
        os.makedirs(outdir, exist_ok=True)
        sample(
            args.jobname,
            seq.seq.__str__(),
            outdir,
            n=args.n,
            msa_depth=args.msa_depth,
            model_id=args.af_model_id,
        )
    

if __name__ == "__main__":

    parser = ArgumentParser()
    
    parser.add_argument("--jobname", type=str, required=True, help="Job name")
    parser.add_argument("--fasta", type=str, required=True, help="Path to fasta file")
    parser.add_argument("--output_dir", type=str, required=True, help="Path to output directory")
    parser.add_argument("--n", type=int, default=1, help="Number of conformers to sample per sequence")
    parser.add_argument("--msa_depth", type=int, default=32, help="Number of sequences to include in MSA")
    parser.add_argument("--af_model_id", type=int, default=2, help="AlphaFold model id")
    
    args = parser.parse_args()
    main()