from StockAnalysisServer import StockAnalysisServer
import datetime
class UserInterface:
    if __name__ == '__main__':
        ticker = input("Enter the name of the stock")
        time_horizon = input("Enter the no of years you wish to invest:")
        base_amount = input("Enter the starting amount you wish to invest:")
        FinalAmount = input("Enter the final amount that you wish to see after " + str(time_horizon) + " :")
        StockAnalysisServer = StockAnalysisServer()
        probablity = StockAnalysisServer.get_expected_stock_return_probablity(ticker,time_horizon,base_amount)
        print(probablity)