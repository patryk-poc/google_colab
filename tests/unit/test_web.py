""" Testing web client with pytest """


class TestWebClient:
    """Test web requests"""

    def test_get_ip(self, client):  # pylint: disable=no-self-use
        """
        Given: a web client
        When: a GET request is sent to /ip endpoint
        Then: a response with JSON and public IP of the running client is returned
        """
        resp = client.get_ip()
        assert resp.status_code == 200
        assert resp.json()["origin"]
