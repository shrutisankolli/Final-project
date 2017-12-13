import numpy as np
from pandas import DataFrame
from DataReader import DataReader

class DataProcessor:

    def calc_base_rate_and_volatility_by_ticker(self, ticker_data):
        '''
        Calculates the base rate and volatility for the ticker
        :param ticker_data: Input the ticker data
        :return: Base Rate and Volatility
        >>> d = DataReader()
        >>> data = d.fetch_ticker_data('AAPL','20100101')
        >>> p = DataProcessor()
        >>> p.calc_base_rate_and_volatility_by_ticker(data)
        Base Rate is:0.259626145309
        Volatility is:0.25335497362129206
        (0.25962614530885419, 0.25335497362129206)
        '''
        trading_days = (ticker_data.index[-1] - ticker_data.index[0]).days
        base_rate = ((((ticker_data['Adj Close'][-1]) / ticker_data['Adj Close'][1])) ** (
                    365.0 / trading_days)) - 1
        ticker_data['Returns'] = ticker_data['Adj Close'].pct_change()
        volatility = ticker_data['Returns'].std()*(252)**(1/2.0)

        print("Base Rate is:"+str(base_rate))
        print("Volatility is:"+str(volatility))
        return base_rate,volatility

    def calc_expected_return_probablity_based_on_monte_carlo(self, base_rate,volatility,time_horizon, pv,ending_value):
        '''
        Calculates the probability of the achieving the target amount
        :param base_rate:Base return rate for the ticker
        :param volatility: Base volatility for the ticker
        :param time_horizon: The time horizon the user wishes to invest
        :param pv: The initial amount the user wishes to start investment with
        :param ending_value: The end amount the user wishes to see.
        :return:

        '''
        iterations = 5000
        sim = DataFrame()
        returns1 = DataFrame()
        for x in range(iterations):
            annual_investment = 10000
            stream = []
            new_pv=int(pv)
            returns_list = [base_rate]
            for i in range(int(time_horizon)):
                returns = np.random.normal(base_rate, volatility)
                if (returns > returns_list[-1]):
                    a = np.random.normal(annual_investment, 100)
                else:
                    a = 0

                end = round(new_pv * (1 + returns) + a, 2)

                stream.append(end)
                returns_list.append(returns)
                new_pv = end

            sim[x] = stream
            returns1[x] = returns_list
        ending_values = sim.loc[int(time_horizon)-1]
        return ending_values,len(ending_values[ending_values>int(ending_value)]) / len(ending_values)

