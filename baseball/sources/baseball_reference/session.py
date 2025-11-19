from time import sleep

from curl_cffi import requests
from datetime import datetime as dt
from typing import Any, Optional
from utils.singleton import Singleton


BASE_URL = "https://www.baseball-reference.com"


class BaseballReferenceSession(Singleton):
    """
    Baseball reference has limiting to prevent bot traffic. According to their policy only 10
    requests per minute are allowed. This Singleton session can be used to access Baseball Reference
    data within the (10 requests per minute) limit.
    """

    def __init__(
        self,
        max_requests_per_minute: int = 10,
    ) -> None:
        self.max_requests_per_minute = max_requests_per_minute
        self.last_request: Optional[dt] = None
        self.session = requests.Session()

    def get(
        self,
        url: str,
        **kwargs: Any,
    ) -> requests.Response:
        if self.last_request:
            # given the last request determine if we need to sleep for a bit so we still have
            # less than max_requests_per_minute requests per minute
            delta = dt.now() - self.last_request
            sleep_length = (60 / self.max_requests_per_minute) - delta.total_seconds()
            if sleep_length > 0:
                sleep(sleep_length)
        # update the last time we made a request
        self.last_request = dt.now()
        # make the request
        response = self.session.get(
            url,
            impersonate="chrome",
            **kwargs,
        )
        response.raise_for_status()
        return response
