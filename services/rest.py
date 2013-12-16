from bottle import route, run
from services.gmaps.distancematrix import distance

@route('/hello')
def hello():
    result = distance("Boston, MA", "Redmond, WA")
    return result

run(host='localhost', port=8080, debug=True)