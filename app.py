import argparse
import yaml
import numpy as np

def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def load_elevation_matrix(file_path):
    return np.loadtxt(file_path, delimiter=',')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", type=int, required=True)
    parser.add_argument("-y", type=int, required=True)
    parser.add_argument("-H", type=float, required=True)
    parser.add_argument("-r", type=float, required=True)
    parser.add_argument("--config", type=str, default="config.yaml")
    args = parser.parse_args()
    config = load_config(args.config)
    matrix_file_path = config["file_elevation_matrix"]
    elevation_matrix = load_elevation_matrix(matrix_file_path)
    print(args)
    print(elevation_matrix)

if __name__ == "__main__":
    main()