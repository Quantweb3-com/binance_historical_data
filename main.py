import datetime
from binance_historical_data import BinanceDataDumper


def main():
    data_dumper = BinanceDataDumper(
        asset_class="um",  # spot, um, cm
        path_dir_where_to_dump="./cache",
        data_type="klines",  # aggTrades, klines, trades
        data_frequency="1m",  # argument for data_type="klines"
    )

    data_dumper.dump_data(
        tickers='ETHUSDT',
        date_start=datetime.date(year=2022, month=1, day=1),
        date_end=datetime.date(year=2025, month=1, day=19),
        is_to_update_existing=False,
        tickers_to_exclude=["UST"],
    )

if __name__ == "__main__":
    main()
