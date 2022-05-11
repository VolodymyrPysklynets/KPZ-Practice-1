import lab3
def test_palindrom():
    assert lab3.palindrom() == []

    try:
        lab3.palindrom(12)
    except TypeError:
        assert True

    assert lab3.palindrom("php coding") == ["php"]

    assert lab3.palindrom("mum redder wow deed") == [
        "mum", "redder", "wow", "deed"]
    assert lab3.palindrom("lollipop8*(/) 6543456^&%$?") == []
