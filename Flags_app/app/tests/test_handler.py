from app.src.handler import handler

def test_handler_ok():
    resp = handler({"rawPath":"/health"}, None)
    assert resp["statusCode"] == 200
