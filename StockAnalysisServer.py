from DataReader import DataReader
from DataProcessor import DataProcessor
import datetime
from dateutil.relativedelta import relativedelta

class StockAnalysisServer:
    def __init__(self):
        self.data_reader = DataReader()
        self.data_processor = DataProcessor()

    def get_expected_stock_return_probablity(self,ticker_name,time_horizon,base_amount,finalAmount,historic_data_years=1):
        '''
        This method computes the probability of the expected return
        :param ticker_name: The ticker name the user wishes to return
        :param time_horizon:The time horizon the user wishes to invest for
        :param base_amount:The base amount the user wishes to start investing with
        :param finalAmount:The final amount the user wishes to achieve
        :param historic_data_years:The no of years the user wishes to use for base values calculation
        :return:The probability of user achieving the target amount
        '''
        from_date = datetime.date.today() - relativedelta(years=historic_data_years)
        ticker_data = self.data_reader.fetch_ticker_data(ticker_name, from_date)# '1/1/2017'
        base_rate, volatility = self.data_processor.calc_base_rate_and_volatility_by_ticker(ticker_data)
        probablity_expected_return = self.data_processor.calc_expected_return_probablity_based_on_monte_carlo(base_rate,volatility,time_horizon,base_amount,finalAmount)
        return probablity_expected_return