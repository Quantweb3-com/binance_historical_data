from binance_historical_data import BinanceDataDumper

def main():
    um_data_dumper = BinanceDataDumper(
        path_dir_where_to_dump='/usr/local/share/binance_data/cache',
        asset_class='um',
        data_type='liquidationSnapshot',
        save_format='parquet',
    )
    
    um_symbols = um_data_dumper.get_list_all_trading_pairs()
    
    um_data_dumper.dump_data(
        tickers=um_symbols,
        tickers_to_exclude=['UST'],
        is_to_update_existing=False,
    )

if __name__ == '__main__':
    main()
