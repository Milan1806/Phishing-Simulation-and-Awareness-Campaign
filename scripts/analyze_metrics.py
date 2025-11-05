# Run this script from the scripts folder
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../analysis/metrics_anonymized.csv')
agg = df.groupby('cohort').agg(total=('user_id','count'), clicks_pre=('clicked_pre','sum'), clicks_post=('clicked_post','sum')).reset_index()
agg['click_rate_pre'] = agg['clicks_pre'] / agg['total']
agg['click_rate_post'] = agg['clicks_post'] / agg['total']
print(agg)

plt.figure()
plt.bar(agg['cohort'], agg['click_rate_pre'], label='Pre')
plt.bar(agg['cohort'], agg['click_rate_post'], label='Post')
plt.legend()
plt.savefig('../analysis/metrics_plots/click_rate_by_cohort.png')
print('Saved plot')
