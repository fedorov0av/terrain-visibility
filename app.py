import os
import argparse
import yaml
import numpy as np

from backend.utils.visibility import get_visible_area
from backend.utils.data_transform import transform_visible_area_as_polygon_geojson
from backend.setup.config import MATRIX_FILE_PATH, OUTPUT_FILE_PATH

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
    args = parser.parse_args()
    os.makedirs(os.path.dirname(OUTPUT_FILE_PATH), exist_ok=True)
    elevation_matrix = load_elevation_matrix(MATRIX_FILE_PATH)
    visible_points = get_visible_area(elevation_matrix, args.x, args.y, args.H, args.r)
    transform_visible_area_as_polygon_geojson(visible_points, (args.x, args.y), args.r, args.H, OUTPUT_FILE_PATH)

if __name__ == "__main__":
    main()