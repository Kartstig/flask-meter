import flask
from datetime import datetime
from typing import List, Literal, Callable, Dict, Optional, Union

from .git import git_stats, GitReturn

FuncList = List[Callable]

ResponseJson = Dict[
    Union[Literal["uptime"], Literal["app"], Literal["status"], Literal["git"], str],
    Union[str, Literal["OK"], Literal["DOWN"], GitReturn],
]


class FlaskMeter(object):
    def __init__(
        self, app: Optional[flask.Flask] = None, extra_checks: FuncList = []
    ) -> None:
        if app is not None:
            self.init_app(app, extra_checks)

    def init_app(self, app: flask.Flask, extra_checks: list = []) -> None:
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

        def _health() -> flask.Response:
            data: ResponseJson = {
                "uptime": str(datetime.now() - self.start_time),
                "app": self.app.name,
            }

            raw_results: List[bool] = []
            if extra_checks:
                results = {}
                for func in extra_checks:
                    try:
                        res: bool = func()
                        raw_results.append(res)
                    except:
                        res = False

                    results[func.__doc__] = "OK" if res else "DOWN"
                data.update(results)

            data["status"] = "OK" if all(raw_results) else "DOWN"

            if self.app.config["FLASK_METER_GIT"]:
                data.update({"git": git_stats()})

            return flask.jsonify(data)

        if self.app.config["FLASK_METER_ENABLE"]:
            self.app.add_url_rule("/_health", "_health", _health)
