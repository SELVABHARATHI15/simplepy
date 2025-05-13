from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde", kde=True, bins=20, color="red", label="Normal")

plt.show()