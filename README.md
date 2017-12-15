Create a FORK of this repository to store your code, data, and documentation for the final project. Detailed instructions for this assignment are in the course Moodle site.  The reason I'm asking you to fork this empty repository instead of creating a stand-alone repository is that it will be much easier for me and all students in the course to find all of our projects for code review and for grading. You can even get code review from students in the other section of IS590PR this way.

Even though your fork of this repository shall remain public, you'll still need to explicitly add any students on your team as Collaborators in the Settings. That way you can grant them write privileges.

DELETE the lines from TEMPLATE up.

TEMPLATE for your report:

# Title: 
Monte Carlo Simulation in Python for the simulation of a Random Walk.

## Team Member(s):
1. Shruti S. Sankolli
2. Shraddha Machchhar
3. Sayali Tamble

(Note: Don't put your email addresses here (which is public).  If a student wants their NAME hidden as well, due to optional FERPA regulations, they can be listed purely by their GitHub ID).

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

## Sources Used:
https://www.investopedia.com/articles/07/montecarlo.asp
