import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Excel Data read
df = pd.read_csv("student_scores csv.csv")
print(df.head())
df.describe()
df.info()
df.isnull().sum()

# drop unnamed column

df = df.drop("Unnamed: 0",axis=1)
print(df.head())

# change wekkly study hours columns

df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-oct","5-10")
print(df.head())

# Gneder distribuation
plt.figure(figsize = (5,5))
sns.countplot(data=df,x= "Gender")
plt.show()

# from the above chart we have analyzed that the number of females in the data is more than the numbers of names

gb = df.groupby("ParentEduc"). agg({"MathScore":'mean',"ReadingScore":"mean","WritingScore":"mean"})
plt.figure(figsize=(8,6))
print(gb)
plt.title("Realationship between parents education and students score")
sns.heatmap(gb, annot= True)
plt.show()

# From the above chart we have consuled that the education of the parents have a good impact their students

gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
plt.figure(figsize=(4,4))
plt.title("Relationship between parents's Education and student's score")
sns.heatmap(gb1, annot= True)
plt.show()
print(gb1)

# from the above chart we have concluded that there is no neligable impact on the students schedule due to thair parents maritual students
sns.boxplot(data=df,x="MathScore")
plt.show()
sns.boxplot(data=df,x="ReadingScore")
plt.show()
sns.boxplot(data=df,x="WritingScore")
plt.show()

#wekkly study hour reports check

sns.boxplot(data= df, x= "WklyStudyHours")
plt.show()

# nr siblings check reports
sns.boxenplot(data=df,x="NrSiblings")
plt.show()

print(df["EthnicGroup"].unique())

#Distribution of Ethnicgroups

ethnic_counts = df["EthnicGroup"].value_counts()
plt.pie(ethnic_counts, labels=ethnic_counts.index, autopct="%1.2f%%")
plt.title("Distribution of Ethnic Groups")
plt.show()

# Countplot for EthnicGroup with labels
ax = sns.countplot(data=df, x='EthnicGroup')
ax.bar_label(ax.containers[0])
plt.title("Ethnic Group Distribution")
plt.show()

# Final check of unique EthnicGroups
print(df["EthnicGroup"].unique())

