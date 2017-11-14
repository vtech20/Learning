# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 10:30:48 2017

@author: baradhwaj
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf
os.getcwd()
os.chdir("G:\Python\Learning\Lectures\Day-10\Data")
catsData = pd.read_csv("cats.csv",thousands =',')
print(catsData)
#Step-2:
plt.scatter("Bwt","Hwt",data=catsData)
plt.xlabel("Body Weight(kg)")
plt.xlabel("Heart Weight(g)")

cat_3kg = catsData.loc[(catsData["Bwt"]>3)&(catsData["Bwt"<= 4])]
np.mean(cat_3kg["Hwt"])

# Hwt = m* Bwt +C

# Step3: Correlation analysis
# Co varianc helps measuing the releationship between variables
# Co var depends on the scale of data
# corrlelation is scaled co variance ranging -1 and 1
# -1 : String neg corr
# +1: Strong pos corr
# 0 - No corr  Note: -.5 to 0 to +.5 is the scale to inform no corr can be done
## Proceed with reg wien there is reasonably strong corr
np.mean(catsData["Bwt"])
np.var(catsData["Bwt"])
np.std(catsData["Bwt"])
catsData["Bwt"].cov(catsData["Hwt"])
catsData["Bwt"].corr(catsData["Hwt"])
#  Step 4 : Build regression model
#formula :DV ~IDV
cats_simple_linear_model = smf.ols(formula='Hwt ~ Bwt', data = catsData).fit()
cats_simple_linear_model.summary()
## Hwt = m* Bwt +C
# formula : 4.0341 * Bwt -0.3567
Bwt = 3.7
predicted_Hwt = 4.0341 * Bwt -0.3567
actual_wt = 11
abs(actual_wt -predicted_Hwt )/actual_wt # 32.4 % deviation


### Home work ##########
##Dv : wg, IDV: metmin
