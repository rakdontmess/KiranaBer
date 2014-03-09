import urllib
import json

DISTANCE_BASE_URL = "http://maps.googleapis.com/maps/api/distancematrix/json?%s"

def distance(origin, destination):
    url = construct_distance_url(origin, destination)
    data = json.loads(url.read().decode("utf-8"))
    return data["rows"][0]["elements"][0]["distance"]["text"]
    
def construct_distance_url(origin, destination):
    params = urllib.urlencode({ "origins" : origin, "destinations" : destination, "sensor" : "false"})
    return urllib.urlopen(DISTANCE_BASE_URL % params)