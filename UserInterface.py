from StockAnalysisServer import StockAnalysisServer
import datetime
import matplotlib.pyplot as plt
class UserInterface:
    if __name__ == '__main__':
        ticker = input("Enter the name of the stock")
        time_horizon = input("Enter the no of years you wish to invest:")
        base_amount = input("Enter the starting amount you wish to invest:")
        finalAmount = input("Enter the final amount that you wish to see after " + str(time_horizon) + " :")
        StockAnalysisServer = StockAnalysisServer()
        dist,probablity = StockAnalysisServer.get_expected_stock_return_probablity(ticker,time_horizon,base_amount,finalAmount)
        print(probablity)
        plt.hist(dist)
        plt.show()