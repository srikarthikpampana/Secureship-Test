from app import app


def test_index_renders_default_name():
    resp = app.test_client().get("/")
    assert resp.status_code == 200
    assert b"Hello world" in resp.data


def test_user_input_is_escaped():
    resp = app.test_client().get("/?name=<script>x</script>")
    assert b"<script>" not in resp.data
    assert b"&lt;script&gt;" in resp.data
