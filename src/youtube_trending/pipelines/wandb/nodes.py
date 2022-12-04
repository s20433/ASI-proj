"""
This is a boilerplate pipeline 'wandb'
generated using Kedro 0.18.3
"""

import wandb

def run_wandb(models, n_estimators, max_depth):
    '''Odpala cały potok wandb

    '''
    wandb.config.n_estimators = n_estimators
    wandb.config.max_depth = max_depth
    wandb_start = wandb.init(project="wandb-and-youtube-vids")

    return wandb_start