from math import radians, sin, cos, sqrt, asin

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified with longitude and latitude in decimal degrees)
    """
    # 将十进制度数转换为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # 地球半径（千米）
    R = 6371.0

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    
    return R * c


if __name__ == '__main__':
    distance = haversine(116.3971, 39.9074, 121.4737, 31.2304)
    print(f"Distance: {distance:.2f} km")