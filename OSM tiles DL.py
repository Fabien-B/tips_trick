import math
from urllib.request import urlopen

directory='tiles'

def dl_tile(X,Y,zoom):
	url = 'http://tile.openstreetmap.org/%d/%d/%d.png' % (zoom,X, Y)
	print(url)
	path = '{}/({}, {}, {}).png'.format(directory,X,Y,zoom)
	with open(path, 'wb') as img:
		img.write(urlopen(url).read())

def dl_zone(Xmin,Xmax,Ymin,Ymax,zoom):
	for X in range(Xmin,Xmax+1):
		print('{} / {}'.format(X-Xmin,Xmax-Xmin))
		for Y in range(Ymin,Ymax+2):
			print("dl")
			dl_tile(X,Y,zoom)

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

def dl_zone_lat_lon(lat1,lon1,lat2,lon2,zoom):
	c1 = get_tile_nbs(zoom, lat1, lon1)
	c2 = get_tile_nbs(zoom, lat2, lon2)
	Xmin,Ymin = c1
	Xmax, Ymax = c2
	if Xmin>Xmax:
		Xmin, Xmax = Xmax, Xmin
	if Ymin>Ymax:
		Ymin, Ymax = Ymax, Ymin
	print("Xmin: {}, Xmax: {}, Ymin:{}, Ymax:{}".format(Xmin,Xmax,Ymin,Ymax))
	dl_zone(Xmin,Xmax,Ymin,Ymax,zoom)

