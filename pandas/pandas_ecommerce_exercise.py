# average purchase price?
df['Purchase Price'].mean()

# ** How many people have English 'en' as their Language of choice on the website? **
df[df['Language'] == 'en'].shape[0]

# ** How many people have the job title of "Lawyer" ? **
sum(df['Job'].apply(lambda x: x.lower() == 'lawyer'))

# purchase by AM / PM
df['AM or PM'].value_counts()

# 5 post popular jobs
df['Job'].value_counts()[0:5]

# name of guy who made purchase with this numberdf
[df['Credit Card'] == 4926535242672853].Name
