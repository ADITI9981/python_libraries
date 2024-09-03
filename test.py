#suppose the IQ in a certain population is normally distributed with a mean of  u=100 amd standard
#deviation of 15.

#A researchers wants to know if a new drug affects IQ levels, so he recruits 20 patients to try it and
#record their IQ levels.

#the following code shows how to perform a one sample z-test in python to determine if the new drug
#causes a significant difference inIQ levels.

from statsmodels.stats.weightstats import ztest as ztest

#enter IQ levels for 20 patients
data=[88,92,94,94,96,97,97,97,99,99,
      105,109,109,109,110,112,112,113,114,115]

ztest(data,value=100)

## t-test
ages=[10,20,35,50,28,40,55,18,16,55,30,25,43,18,30,28,14,24,16,17,32,35,26,27,65,18,43,23,21,19,70]
import numpy as np
ages_mean=np.mean(ages)
ages_mean

sample_size=10
age_sample=np.random.choice(ages,sample_size)

age_sample

from scipy.stats import ttest_1samp

np.mean(age_sample)

ttest_1samp(age_sample,30)

TtestResult(statistic=-1.4696938456699067, pvalue=0.17571476562743057, df=9)

import numpy as np
import pandas as pd
import scipy.stats as stats
import math
np.random.seed(6)

school_ages=stats.poisson.rvs(loc=18,mu=35,size=1500)
class_ages=stats.poisson.rvs(loc=18,mu=30,size=60)

school_ages

class_ages

class_ages.mean()

_,p_value=ttest_1samp(class_ages,popmean=school_ages.mean())

if p_value<0.05:
    print("reject h0")
else:
    print("accept h0")


import seaborn as sns

df=sns.load_dataset('iris')
df.head()

sns.pairplot(df)