import pandas as pd
sal = pd.read_csv('salaries.csv')
sal.head()
sal.info()

# remove nan and string values
# get average of base salary
a = a['BasePay'].apply(pd.to_numeric, errors='coerce').dropna().mean()

# get highest paid guy
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']
# or...
sal.loc[sal['TotalPayBenefits'].idxmax()]

# lowest paid
sal.loc[sal['TotalPayBenefits'].argmin()]

# mean pay by year
sal.groupby('Year').mean()

# num. uniqut titles
sal['JobTitle'].nunique()

# top 10 job titles
sal['JobTitle'].value_counts()[0:10]

# job titles with 1 count in 2013
sum(sal[sal.Year == 2013].JobTitle.value_counts() == 1)

# any title with 'chief'
sum(sal['JobTitle'].apply(lambda x: fun_if_includes_chief(x)))

# correlation between len(JobTitle) and salary?
# apply is like JavaScript apply
sal['title_len'] = sal['JobTitle'].apply(len)
# no correlation...obv.
sal[['TotalPayBenefits', 'title_len']].corr()
# below is 1. Of course.

# Also 1.
sal[['OvertimePay', 'Year']].corr()

sal[['JobTitle', 'title_len']].corr()

