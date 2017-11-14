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
import seaborn
# DV: HWT  IDV : BWT
# Step 1 : 
os.getcwd()
os.chdir("G:\Python\Learning\Lectures\Day-10\Data")
catsData = pd.read_csv("cats.csv",thousands =',')
print(catsData)
#Step-2:
plt.scatter("Bwt","Hwt",data=catsData)
plt.xlabel("Body Weight(kg)")
plt.ylabel("Heart Weight(g)")
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
# Step 1 
os.chdir('G:\Python\Learning\Lectures\Day-6\data')
weightGain = pd.read_csv("wg.csv",thousands =',')
print(weightGain)
# Step2
plt.scatter("metmin" ,"wg",data=weightGain)
plt.ylabel("Weight Gain (g)")
plt.xlabel("Metmin")
# Step 3  correletion : -0.90625914221504655
weightGain["metmin"].corr(weightGain["wg"]) 
# Step 4: 
wg_linear_model = smf.ols(formula='wg ~ metmin', data = weightGain).fit()
wg_linear_model.summary()
# Formula: Wg = m* metmin + C
# Substitution : wg =-0.0189*metmin +54.1624
#15 , 	1790
metmin = 1790
predictedwg = -0.0189*metmin +54.1624
print(predictedwg)
actualWg = 15
abs(actualWg -predictedwg )/actualWg # 35.54 % deviation
# how much deviation is permissable / can be used as quantifier to assume the data is correct and proceed?
