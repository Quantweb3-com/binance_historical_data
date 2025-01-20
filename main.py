import datetime
from binance_historical_data import BinanceDataDumper


def main():
    data_dumper = BinanceDataDumper(
        asset_class="um",  # spot, um, cm
        path_dir_where_to_dump="./cache",
        data_type="klines",  # aggTrades, klines, trades
        data_frequency="1m",  # argument for data_type="klines"
    )
    
    symbols = data_dumper.get_list_all_trading_pairs()

    data_dumper.dump_data(
        tickers=symbols,
        is_to_update_existing=False,
        tickers_to_exclude=["UST"],
    )

if __name__ == "__main__":
    main()
