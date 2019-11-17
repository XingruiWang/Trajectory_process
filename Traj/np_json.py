import numpy as np
import json

#traj = np.load('D:/文档/6_项目/3_荣誉辅修/数据/Data/000/Trajectory/20081023025304.npy', allow_pickle=True)
def np2json(traj):
    out = []
    start_time = 1573617600
    for i in traj:
        d = {"longitude": float(i[1]), "latitude": float(i[0]), "coord_type_input": "wgs84", "loc_time": start_time}
        start_time += 50
        out.append(d)
    out = json.dumps( out )

    return out

def json2np(traj_json):
    print(json.load(traj_json[0]))


