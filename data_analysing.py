# https://www.dataquest.io/blog/how-to-analyze-survey-data-python-beginner/

import pandas as pd

df = pd.read_csv('survey_results_public.csv')

print(df.head())
print(df.shape)
print(df['RemoteWork'].value_counts())
