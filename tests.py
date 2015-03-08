import dataio


def test_parse_timestamp():
    expected = dict(year=2012, month=12, day=19, hour=23)
    result = dataio.parse_timestamp('2012-12-19 23:00:00')
    for key in expected:
        assert key in result
        assert result[key] == expected[key], (key, result[key], expected[key])
