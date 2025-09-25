import yaml
import os
from pathlib import Path

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(PROJECT_PATH, "config.yaml"), "r") as f:
    cfg = yaml.safe_load(f)
MODELS = cfg.get('models')

if __name__ == '__main__':
    print(PROJECT_PATH)
    print(MODELS, type(MODELS))
