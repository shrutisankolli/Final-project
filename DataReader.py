from pandas import pandas,Series,DataFrame
from pandas_datareader import data

class DataReader:

    def fetch_ticker_data(self,tickerName,fromDate):
        '''
        This function makes the call to the Yahoo stocks API to fetch the ticker data.
        '''
        ticker_data = data.DataReader(tickerName, 'yahoo', start=fromDate)
        return ticker_data
