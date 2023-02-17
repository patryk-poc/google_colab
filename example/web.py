""" Simple module to test web requests with pytest """
import requests


class Web:
    """A simple web client"""

    def __init__(self, url: str = "https://httpbin.org") -> None:
        self.url = url
        self.session = self.configure_session()

    def configure_session(self) -> requests.Session:
        """Get a session object"""
        _session = requests.Session()
        _session.trust_env = False
        return _session

    def get_ip(self):
        """Get a client public IP"""
        return self.session.get(self._url("ip"))

    def _url(self, path: str):
        """Build URL"""
        return f"{self.url}/{path}"
