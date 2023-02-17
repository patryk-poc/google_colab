from unittest.mock import Mock, patch

from example.web import Web


def test_get_ip():
    mock_response = Mock()
    mock_response.text = "1.2.3.4"
    mock_get = Mock(return_value=mock_response)

    with patch.object(Web, "configure_session") as mock_configure_session:
        mock_session = Mock()
        mock_session.get = mock_get
        mock_configure_session.return_value = mock_session

        client = Web()
        ip = client.get_ip()
        assert ip.text == "1.2.3.4"
        mock_get.assert_called_once_with("https://httpbin.org/ip")


def test_get_ip_chaining_method_calls():
    mock_response = Mock(text="1.2.3.4")
    mock_session = Mock(get=Mock(return_value=mock_response))

    with patch.object(Web, "configure_session", return_value=mock_session):
        ip = Web().get_ip()
        assert ip.text == "1.2.3.4"
        mock_session.get.assert_called_once_with("https://httpbin.org/ip")
