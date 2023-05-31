import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://8d4756348705430590f9229f76963c6a@o4505275453800448.ingest.sentry.io/4505275941257216",
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0