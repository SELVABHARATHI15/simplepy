from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = sns.displot(random.binomial(n=25,p=0.5,size=10))
plt.show()
