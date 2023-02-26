from altquant.simulator.trade_index import TradeDate, TradeIndex
import pytest

def test_index_creation():
    """Tests the creation of the TradeIndex class"""
    ti = TradeIndex()

    ti._set_dates(['2021-01-01', '2021-01-02', '2021-01-03'], format='YYYY-MM-DD')

    check_trade_index_dates = tuple([
        TradeDate(year=2021, month=1, day=1),
        TradeDate(year=2021, month=1, day=2),
        TradeDate(year=2021, month=1, day=3)
    ])
    assert ti.dates == check_trade_index_dates, 'TradeIndex yields incorrect dates!'