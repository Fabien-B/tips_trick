import math
def get_tile_nbs(zoom, lat, lon):
        zn = float(1 << zoom)
        tx = float(lon + 180.0) / 360.0
        latrad = lat * math.pi / 180.0
        ty = 0.5 - (0.5/math.pi)*math.log(math.tan(latrad) + 1.0 / math.cos(latrad))
        X = int(tx * zn)
        Y = int(ty * zn)
        #resX = tx * zn - X
        #resY = ty * zn - Y
        return (X, Y)
