
import requests

class SmoothenRoads():

    def __init__(self):
        self.api_key = 'DofzdMRY0OEZeKlQgocFFYXlhVNLAxpa'

    def get_smoth_roads(self, points):
        #req = requests.get(
         #   'http://api.map.baidu.com/rectify/v1/track?point_list=%s&ak=%s' %(points, self.api_key))

        r = requests.post('http://api.map.baidu.com/rectify/v1/track?', data={'ak':self.api_key, 'point_list':points})
        #points = req.json().get('points')
        return r.json().get('points')

sr = SmoothenRoads()

print(sr.get_smoth_roads(points))