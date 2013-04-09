#!/usr/bin/python
from apiserver  import app
#Start server on all network interfaces and in DEBUG mode
app.run(debug=True,host='0.0.0.0')
