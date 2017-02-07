import pandas as pd
import seaborn as sns

sns.set()
d = pd.read_csv('data.csv')
d.columns = ['state', 'population', 'density', 'suicide']
d.density = [float(x.replace(',', '')) for x in d.density]
d['size'] = [1000 * ((p / max(d['population']))**1.2) + 1000 for p in d.population]
print(d['size'])
p = sns.regplot(x=d.density, y=d.suicide, order=2, scatter_kws={'s':d['size']})

"""
for row in d.itertuples():
    if row[2] > 12000000:
        p.annotate(row[1], (row[3], row[4] + (row[5]/2000)))
        """

p.set(xlabel="Population Density (persons per square mile)", ylabel="Suicides per 100,000 people", title="Suicide vs Population Density")
        
sns.plt.show()
