import os
import argparse
import yaml
import numpy as np

from utils.visibility import get_visible_area
from utils.data_transform import save_visible_area_as_polygon_geojson


def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def load_elevation_matrix(file_path):
    return np.loadtxt(file_path, delimiter=',')

def main():
    parser = argparse.ArgumentParser(
        description="Calculate visible area from a given observer position over an elevation matrix.",
        epilog="""\
Exapmple usage:
    python3 app.py -x 10 -y 20 -H 5 -r 10 --config config.yaml
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-x", type=int, required=True, help="X coordinate of the point")
    parser.add_argument("-y", type=int, required=True, help="Y coordinate of the observer")
    parser.add_argument("-H", type=float, required=True, help="Height of the observer")
    parser.add_argument("-r", type=float, required=True, help="Radius of the observer's visibility")
    parser.add_argument("--config", type=str, default="config.yaml")
    args = parser.parse_args()
    config: dict = load_config(args.config)
    matrix_file_path = config["file_elevation_matrix"]
    output_file_path = config["file_output"]
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    elevation_matrix = load_elevation_matrix(matrix_file_path)
    visible_points = get_visible_area(elevation_matrix, args.x, args.y, args.H, args.r)
    print('visible_points: ', visible_points)
    save_visible_area_as_polygon_geojson(visible_points, (args.x, args.y), args.r, args.H, output_file_path)

if __name__ == "__main__":
    main()