from pandas import pandas,Series,DataFrame
from pandas_datareader import data

class DataReader:

    def fetch_ticker_data(self,tickerName,fromDate):
        '''
        This method fetches the data for the input ticker from Yahoo
        :param tickerName:The ticker name the user wishes to invest in
        :param fromDate:The date from ehich the user wishes to start observing the price to compute base return and volatility
        :return:Ticker Data
        '''
        ticker_data = data.DataReader(tickerName, 'yahoo', start=fromDate)
        return ticker_data
