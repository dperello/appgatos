from bottle import route, run, template
from datetime import datetime


@route('/hello')
def hello():
  dt=datetime.now()
  time="{:%Y-%m-%d}".format(dt)
  return template("<b>Helloss</b> {{t}} World!",t=time)


run(host='appgatos-serviphone.rhcloud.com', port=80, debug=True)
