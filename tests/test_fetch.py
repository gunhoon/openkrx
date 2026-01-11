import pytest

from openkrx.fetch import get


@pytest.mark.skipif(False, reason="Not implemented")
def test_get():
    svc_nm = 'idx'
    api_id = 'krx_dd_trd'
    date = '20260108'

    data = get(svc_nm, api_id, date)
    for x in data:
        print(x)
