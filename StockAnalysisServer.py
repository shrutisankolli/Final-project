from DataReader import DataReader
from DataProcessor import DataProcessor
import datetime
from dateutil.relativedelta import relativedelta

class StockAnalysisServer:
    def __init__(self):
        self.data_reader = DataReader()
        self.data_processor = DataProcessor()

    def get_expected_stock_return_probablity(self,ticker_name,time_horizon,base_amount, historic_data_years=1):
        from_date = datetime.date.today() - relativedelta(years=historic_data_years)
        ticker_data = self.data_reader.fetch_ticker_data(ticker_name, from_date)# '1/1/2017'
        base_rate, volatility = self.data_processor.calc_base_rate_and_volatility_by_ticker(ticker_data)
        probablity_expected_return = self.data_processor.calc_expected_return_probablity_based_on_monte_carlo(base_rate,volatility,time_horizon,base_amount)
        return probablity_expected_return