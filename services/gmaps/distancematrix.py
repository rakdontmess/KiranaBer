import urllib.parse
import urllib.request
import json

DISTANCE_BASE_URL = "http://maps.googleapis.com/maps/api/distancematrix/json?"

def distance(origin, destination):
    url = construct_distance_url(origin, destination)
    data = urllib.request.urlopen(url)
    data = json.loads(data.read().decode("utf-8"))
    return data["rows"][0]["elements"][0]["distance"]["text"]
    
def construct_distance_url(origin, destination):
    url = []
    url.append(DISTANCE_BASE_URL)
    params = { "origins" : origin, "destinations" : destination, "sensor" : "false"}
    url.append(urllib.parse.urlencode(params))
    return ''.join(url)