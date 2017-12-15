# Title: 
Monte Carlo Simulation in Python for the simulation of a Random Walk.

## Team Member(s):
1. Shruti S. Sankolli
2. Shraddha Machchhar
3. Sayali Tamble

# Monte Carlo Simulation Scenario & Purpose:
This involves predicting whether we can get profit/positive returns by investing in stocks.
This would involve predicting what kind of returns we can expect by investing in stocks with what kind of probability. We are estimating the expected level of return  and variance of the stock in question. We are also checking the probability of achieveing a target amount by investing in stocks.

### Hypothesis before running the simulation:
Before running the simulation: We assume that we will always see profit and get high probability of reach our target amount.

After running the simulation: We do not always get profit and we dont always reach the target amount.

We have taken into consideration the profit and loss predicted by the simulation on investing in stocks.
To handle this we have considered the below:
We have considered the edge cases of probabilties of profit as well as loss being predicted for the user.
It may happen that there is profit predicted for the ticker of GOOG but loss predicted or generated for any other ticker.
So, we have taken into consideration all these cases.

### Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). 
For each such variable, how did you decide the range and which probability distribution to use?  
Do you think it's a good representation of reality?

We are going to use pseudo-random number generator for the following variables:
1. Market return for the said stock
2. Money re-invested in the stock per year

### Instructions to use the program:
1. Provide the following user Inputs:
a. Ticker name [Valid tickers are AAPL, GOOG, IBM etc]
b. The no of years you wish to invest
c. The initial investment amount
d. The target amount you wish to achieve.

2. The program will fetch the ticker price for the past 1 year and compute a base return rate and colatility rate.

3. The program will then generate Monte Carlo simulations for 'n' no of years.

4. It will generate the following outputs:
a. Probability of reaching the target amount starting with inital amount in t years.
b. Distribution of the Monte Carlo returns for the last year of the time duration.

## Sources Used:
https://www.investopedia.com/articles/07/montecarlo.asp
