import numpy as np
from fastapi import APIRouter, Query

from backend.utils.data_transform import transform_visible_area_as_polygon_geojson
from backend.utils.visibility import get_visible_area
from backend.app import config

matrix_file_path = config["file_elevation_matrix"]
elevation_matrix = np.loadtxt(matrix_file_path, delimiter=',')

router = APIRouter(prefix="/api", tags=["visibility"])

@router.get("/visibility")
def get_visibility(
    x: int = Query(..., description="Координата X станции"),
    y: int = Query(..., description="Координата Y станции"),
    h: int = Query(..., description="Высота станции над уровнем земли"),
    r: int = Query(..., description="Радиус видимости")
):
    visible_points = get_visible_area(elevation_matrix, x, y, h, r)
    feature = transform_visible_area_as_polygon_geojson(
        points=visible_points,
        observer=(x, y),
        radius=r,
        height=h,
        output_path=None
    )
    return feature