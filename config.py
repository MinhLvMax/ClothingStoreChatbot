import yaml
import os
from pathlib import Path

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(PROJECT_PATH, "config.yaml"), "r") as f:
    cfg = yaml.safe_load(f)

MODELS = cfg.get('models')
MODEL = cfg.get('models')[3] # Du an nay dung 1 model dau tien thoi

db_config = cfg.get('db_config')
MYSQL_USER = db_config.get('MYSQL_USER')
MYSQL_PASS = db_config.get('MYSQL_PASS')
MYSQL_HOST = db_config.get('MYSQL_HOST')
MYSQL_PORT = db_config.get('MYSQL_PORT')  # Cổng mặc định của MySQL
MYSQL_DB = db_config.get('MYSQL_DB')

endpoint = cfg.get('endpoint')
PRODUCTS_endpoint = endpoint.get('PRODUCTS')
ORDER_STATUS_endpoint = endpoint.get('ORDER_STATUS')

if __name__ == '__main__':
    print(PROJECT_PATH)
    print(MODELS, type(MODELS))
