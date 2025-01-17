#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --gres=gpu:tesla:1
#SBATCH --time=64:00:00
#SBATCH --mem=10GB
#SBATCH --job-name=mamba_diffusion
#SBATCH --output=./outputs/job_%j.log

#SBATCH -A mamba_diffusion

nvidia-smi

python run.py --config config/image2image.json --phase train
