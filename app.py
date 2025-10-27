from flask import Flask
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

# Configure X-Ray
xray_recorder.configure(service='xray-ecs-demo')
XRayMiddleware(app, xray_recorder)

@app.route('/')
def index():
    return "Hi Lingesh Hope you are doing good!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
