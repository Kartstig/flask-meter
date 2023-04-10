import flask
from datetime import datetime
from typing import List, Callable

from .git import git_stats

FuncList = List[Callable]


class FlaskMeter(object):
    def __init__(self, app: flask.Flask = None, extra_checks: FuncList = []) -> None:
        if app is not None:
            self.init_app(app, extra_checks)

    def init_app(self, app: flask.Flask, extra_checks: list = []):
        if not isinstance(app, flask.Flask):
            raise TypeError("Not a Flask Application")

        self.app = app
        self.app.config["FLASK_METER_ENABLE"] = self.app.config.get(
            "FLASK_METER_ENABLE", True
        )
        self.app.config["FLASK_METER_GIT"] = self.app.config.get(
            "FLASK_METER_GIT", True
        )
        self.start_time = datetime.now()

        def _health():
            data = {
                "status": "OK",
                "uptime": str(datetime.now() - self.start_time),
                "app": self.app.name,
            }

            if extra_checks:
                extra_results = {
                    func.__doc__: "OK" if func() else "DOWN" for func in extra_checks
                }
                data.update(extra_results)

            if self.app.config["FLASK_METER_GIT"]:
                data.update({"git": git_stats()})

            return flask.jsonify(data)

        if self.app.config["FLASK_METER_ENABLE"]:
            self.app.add_url_rule("/_health", "_health", _health)
