import logging

import hydra
from omegaconf import DictConfig

from cutmix import run as cut_mix_run
from experiment import run
from mixup import run as mix_run

__all__ = {
    "experiment": run,
    "mixup": mix_run,
    "cutmix": cut_mix_run,
}

log = logging.getLogger(__name__)


@hydra.main(config_path="conf", config_name="config")
def run_model(cfg: DictConfig) -> None:
    # extract the function to run from the config
    log.info(f"train using {cfg.run}.py")
    run_fn = __all__[cfg.run]
    # run training job
    run_fn(cfg, logger=log)


if __name__ == "__main__":
    """
    Main script to run a training job from the terminal.
    Update/modify the config files in conf and run this script
    to start a training job.

    Usage :
        ! python hydra_run.py --config_path conf --config_name config
    """
    run_model()
