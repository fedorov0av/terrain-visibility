import yaml

def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

config: dict = load_config('backend/setup/config.yaml')
MATRIX_FILE_PATH = config["file_elevation_matrix"]
OUTPUT_FILE_PATH = config["file_output"]