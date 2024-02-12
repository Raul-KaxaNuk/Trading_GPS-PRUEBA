import os 
import pandas as pd
import mplfinance as mpf
data_path = "C:/Users/lizro/Downloads/Data_and_Features"



def dict_data(data_path):
    list_stocks = os.listdir(data_path)
    
    repositorio_stocks = {}
    
    for ticker in list_stocks:
        path = os.path.join(data_path, ticker)
        ticker_name = os.path.splitext(ticker)[0]
        repositorio_stocks[ticker_name] = pd.read_csv(path)
    
    return repositorio_stocks


def custom_chart(df, sve_fig = True, file_name):
    
    renombre de columnas
    
    fig, ax = mpf.plot(BAC_df,
                       type='candle', 
                       volume=True, 
                       title='Bank Of America Stocks January 2022 - December 2023', 
                       figsize=(10, 6)
                       save_fig = True
                       name= f'{file_name}')
    
    return ax