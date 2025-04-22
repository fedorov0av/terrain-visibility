from math import sqrt

def is_visible(altitude_map, station, target, station_height):
    x0, y0 = station
    x1, y1 = target
    dx = x1 - x0
    dy = y1 - y0
    distance = sqrt(dx**2 + dy**2)
    steps = int(distance * 2)
    z_station = altitude_map[y0, x0] + station_height
    for i in range(1, steps):
        t = i / steps
        xi = int(round(x0 + dx * t))
        yi = int(round(y0 + dy * t))
        if not (0 <= xi < altitude_map.shape[1] and 0 <= yi < altitude_map.shape[0]):
            continue
        z_target = altitude_map[yi, xi]
        z_interp = z_station + (altitude_map[y1, x1] - altitude_map[y0, x0]) * t
        if z_target > z_interp:
            return False
    return True

def get_visible_area(altitude_map, x, y, h, r):
    r = int(r)
    visible_points = []
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < altitude_map.shape[1] and 0 <= ny < altitude_map.shape[0]:
                if dx ** 2 + dy ** 2 <= r ** 2:
                    if is_visible(altitude_map, (x, y), (nx, ny), h):
                        visible_points.append((nx, ny))
    return visible_points
