import pandas as pd

survey_url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/steak-survey/steak-risk-survey.csv'
survey = pd.read_csv(survey_url)

survey = survey.drop(0).reset_index(drop=True)

survey = survey.drop(survey.columns[[0, 1]], axis=1)

null_rows = survey.isnull().any(axis=1).sum()

survey = survey.dropna(how='all')

print(survey.head)
