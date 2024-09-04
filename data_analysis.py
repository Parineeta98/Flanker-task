import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = 'D:\Flanker_Experiment\Combined_data2.xlsx'
df = pd.read_excel(data)
#convert df to dataframe
df_data = pd.DataFrame(df)

#ANOVA for reaction time vs type 
model = ols('reaction_time ~ type', data=df_data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
# print(anova_table)

# get mean reaction time for each type
con_mean = df_data[df_data['type'] == 'con']['reaction_time'].mean()
neu_mean = df_data[df_data['type'] == 'neu']['reaction_time'].mean()
incon_mean = df_data[df_data['type'] == 'incon']['reaction_time'].mean()

# get standard deviation for each type
con_std = df_data[df_data['type'] == 'con']['reaction_time'].std()
neu_std = df_data[df_data['type'] == 'neu']['reaction_time'].std()
incon_std = df_data[df_data['type'] == 'incon']['reaction_time'].std()

# save mean reaction time in ANOVA table
anova_table['con_mean'] = con_mean
anova_table['neu_mean'] = neu_mean
anova_table['incon_mean'] = incon_mean

# save standard deviation in ANOVA table
anova_table['con_std'] = con_std
anova_table['neu_std'] = neu_std
anova_table['incon_std'] = incon_std

# print(anova_table)

# ANOVA line plot
sns.pointplot(data=df_data, x='type', y='reaction_time', ci=68, order=['con', 'neu','incon'], capsize=0.1)

plt.xlabel('Flanker Type')
plt.ylabel('Reaction time (sec)')
plt.title('Reaction Time for Different Flanker Types')

#save figure
plt.savefig('D:\Flanker_Experiment\Results\Flanker_Reaction_Time.png', dpi=300)
#save summary table
anova_table.to_excel('D:\Flanker_Experiment\Results\Flanker_Reaction_Time.xlsx')

