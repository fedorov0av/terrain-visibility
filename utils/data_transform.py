import geojson
from shapely.geometry import Polygon

def save_visible_area_as_polygon_geojson(
        points: list[tuple[int, int]],
        observer: tuple[int, int],
        radius: int, height: int,
        output_path: str
    ) -> None:
    if not points or len(points) < 3:
        print("Недостаточно точек для построения полигона.")
        return
    polygon = Polygon(points).convex_hull
    feature = geojson.Feature(
        geometry=geojson.Polygon([list(polygon.exterior.coords)]),
        properties={
            "observer": observer,
            "radius": radius,
            "height": height
        }
    )
    feature_collection = geojson.FeatureCollection([feature])
    with open(output_path, 'w') as file:
        geojson.dump(feature_collection, file, indent=4)
    print(f"Полигон зоны видимости сохранён в формате GeoJSON: {output_path}")

    