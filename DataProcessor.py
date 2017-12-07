import numpy as np
from pandas import DataFrame

class DataProcessor:

    def calc_base_rate_and_volatility_by_ticker(self, ticker_data):
        '''
        Calculate the base market rate
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
        iterations = 500
        sim = DataFrame()
        returns1 = DataFrame()
        pv=int(pv)
        for x in range(iterations):
            annual_investment = 10000
            stream = []
            returns_list = [base_rate]
            for i in range(int(time_horizon)):
                returns = np.random.normal(base_rate, volatility)
                if (returns > returns_list[-1]):
                    a = np.random.normal(annual_investment, 100)
                else:
                    a = 0

                end = round(pv * (1 + returns) + a, 2)

                stream.append(end)
                returns_list.append(returns)
                pv = end

            sim[x] = stream
            returns1[x] = returns_list
        ending_values = sim.loc[int(time_horizon)-1]
        return len(ending_values[ending_values>int(ending_value)]) / len(ending_values)

