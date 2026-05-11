from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir : Path
    source_dir : Path
    train_dir : Path
    test_dir : Path
    test_size : float
    random_state : int
