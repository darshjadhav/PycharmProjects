import numpy as np
import math

# Data
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

# Declarations
profitMonthly = []
profitTaxed = []
profitMargin = []
goodMonths = []
goodMonthsProfit = []
badMonths = []
badMonthsProfit = []
bestMonth = []
bestMonthProfit = []
worstMonth = []
worstMonthProfit = []
profitMean = 0


# Code

i = 0
for i in range(len(revenue)):
    profitMonthly.append(revenue[i] - expenses[i])
    profitTaxed.append(profitMonthly[i] - (profitMonthly[i] * 0.30))
    profitMargin.append(profitTaxed[i] / revenue[i])

profitMean = np.mean(profitTaxed)

j = 0
for j in range(len(revenue)):
    if profitTaxed[j] >= profitMean:
        goodMonths.append(month[j])
        goodMonthsProfit.append(profitTaxed[j])
    else:
        badMonths.append(month[j])
        badMonthsProfit.append(profitTaxed[j])

bestMonthInd = goodMonthsProfit.index(max(goodMonthsProfit))
bestMonth.append(goodMonths[bestMonthInd])
bestMonthProfit.append(goodMonthsProfit[bestMonthInd])

worstMonthInd = badMonthsProfit.index(min(badMonthsProfit))
worstMonth.append(badMonths[worstMonthInd])
worstMonthProfit.append(badMonthsProfit[worstMonthInd])

