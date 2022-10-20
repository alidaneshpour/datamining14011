from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from unicodedata import numeric
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from math import pi

sns.set(rc={'figure.figsize': [15, 8]}, font_scale=1.6)
#####
df = pd.read_csv('FuelConsumption.csv', index_col=0, na_values=True)

########
# print(df.shape)
# print(df.head())
# # df.drop_duplicates()
# a = sns.kdeplot(df['Age'], fill=True, color='r')
# a.set_xlabel('Age', fontsize=30)
# a.set_ylabel('Density', fontsize=30)
# a.tick_params(labelsize=20)
# plt.axvline(x=np.mean(df['Age']), c='green',
#             ls='--', label='Mean Age of All Players')
# ##a = np.mean(df['Age'])
# ##print(a)
# plt.show()

# #########
# sns.set_style("white")
# sns.set_style("ticks")
# plt.figure(figsize=(10, 5))
# sns.boxplot(x=df["Age"], color="lightblue", width=0.2)
# plt.title("Boxplot of Age")
# sns.despine(left=True)
# plt.show()

########

# physical_attributes = [
#     "Strength",
#     "Stamina"
# ]
# df[physical_attributes].describe()


# f = plt.figure(figsize=(18, 9))
# gs = f.add_gridspec(1, 2)

# with sns.axes_style("white"):
#     sns.set_style("ticks")
#     x = 0
#     y = 0
#     for attr in physical_attributes:
#         ax = f.add_subplot(gs[x, y])
#         sns.histplot(data=df, x=attr, bins=25, kde=True)
#         # sns.kdeplot(data=df, x=numeric, cut=0, fill=True,
#         #             palette="crest", linewidth=0, alpha=.5)
#         plt.title(f"Distribution of {attr}")
#         plt.axvline(x=np.mean(df[attr]), c='red', label=f'Mean {attr}')
#         print(np.mean(df[attr]))
#         plt.xlabel(attr)
#         plt.ylabel("Frequency")
#         plt.legend(loc="upper left")
#         sns.despine(trim=True, offset=5)
#         y += 1
#         if (y % 2) == 0:
#             y = 0
#             x += 1

# f.tight_layout()
# plt.show()
# ############
# sns.set_style("white")
# sns.set_style("ticks")
# plt.figure(figsize=(15, 7))
# boxstr = sns.boxplot(x=df["Strength"], color="red", width=0.3)
# plt.title("Boxplot of Strength", fontsize=60)
# boxstr.set_xlabel("Strength", fontsize=60)
# boxstr.tick_params(labelsize=50)
# sns.despine(left=True)
# plt.show()

# sns.set_style("white")
# sns.set_style("ticks")
# plt.figure(figsize=(15, 10))
# boxsta = sns.boxplot(x=df["Stamina"], color="red", width=0.3)
# boxsta.set_xlabel("Stamina", fontsize=60)
# plt.title("Boxplot of Stamina", fontsize=60)
# boxsta.tick_params(labelsize=50)
# sns.despine(left=True)
# plt.show()

###########
# speed_attributes = [
#     "SprintSpeed",
#     "Agility",
#     "Reactions",
#     "Acceleration"
# ]
# df[speed_attributes].describe()


# f = plt.figure(figsize=(18, 9))
# gs = f.add_gridspec(2, 2)

# with sns.axes_style("white"):
#     sns.set_style("ticks")
#     x = 0
#     y = 0
#     for attr in speed_attributes:
#         ax = f.add_subplot(gs[x, y])
#         sns.histplot(data=df, x=attr, bins=25, kde=True)
#         # sns.kdeplot(data=df, x=numeric, cut=0, fill=True,
#         #             palette="crest", linewidth=0, alpha=.5)
#         plt.title(f"Distribution of {attr}")
#         plt.axvline(x=np.mean(df[attr]), c='red', label=f'Mean {attr}')
#         # print(np.mean(df[attr]))
#         plt.xlabel(attr)
#         plt.ylabel("Frequency")
#         plt.legend(loc="upper left")
#         sns.despine(trim=True, offset=5)
#         y += 1
#         if (y % 2) == 0:
#             y = 0
#             x += 1

# f.tight_layout()
# plt.show()

################
# sns.set_style("white")
# sns.set_style("ticks")
# ax = df[['Reactions',	'SprintSpeed',	'Agility', 'Acceleration']].plot(
#     kind='box', fontsize=30)
# plt.show()

##############
# x = df['Preferred Foot'].value_counts()
# y = ['Right foot', 'Left foot']
# cols = ['g', 'm']
# plt.pie(x, labels=y, colors=cols)
# plt.show()

#############
# x = df['Weak Foot'].value_counts()
# y = ['2', '3', '4', '5']
# #y = [1, 2, 3, 4, 5]
# cols = ['navy', 'gold', 'silver', 'r']
# plt.pie(x, labels=y, colors=cols)
# plt.show()

##################
# skillers = df[(df["Skill Moves"] == 4) | (df["Skill Moves"] == 5)]
# skiller_nations = skillers["Nationality"].value_counts(normalize=True)
# rest = skiller_nations[10:].sum()
# skiller_nations = skiller_nations[:10]
# skiller_nations["Other"] = rest
# pie, ax = plt.subplots(figsize=[12, 12])
# labels = skiller_nations.keys()
# plt.pie(x=skiller_nations, autopct="%.1f%%",
#         labels=labels, pctdistance=0.7, explode=[0.05]*11)
# plt.legend(loc="upper right", fontsize=8)
# #plt.title("Skill moves and countries", fontsize=14)
# plt.show()

####################
# pie, ax = plt.subplots(figsize=[15, 10])
# labels = df["Skill Moves"].value_counts().keys()
# print(labels)
# plt.pie(x=df["Skill Moves"].value_counts(), autopct="%.1f%%",
#         labels=labels, explode=[0.05]*4, pctdistance=0.5)
# plt.legend()
# #plt.title("Proportion of players by skill moves", fontsize=14)
# plt.show()

#############
# skillers = df[(df["Skill Moves"] == 5)]
# skiller_nations = skillers["Nationality"].value_counts(normalize=True)
# rest = skiller_nations[10:].sum()
# skiller_nations = skiller_nations[:10]
# skiller_nations["Other"] = rest
# pie, ax = plt.subplots(figsize=[12, 12])
# labels = skiller_nations.keys()
# plt.pie(x=skiller_nations, autopct="%.1f%%",
#         labels=labels, pctdistance=0.5, explode=[0.07]*11)
# plt.legend(loc="upper right", fontsize=8)
# #plt.title("Skill moves and countries", fontsize=14)
# plt.show()

########
# sns.histplot(df['Overall'])
# plt.show()


#####################
# column_r = ['Name', 'Overall', 'Potential', 'SprintSpeed',
#             'ShotPower', 'ShortPassing', 'Dribbling', 'Stamina', "BallControl"]
# rival = df.head(2)[column_r]
# rival = rival.set_index('Name')
# rival.head()


# values = rival.iloc[0].tolist()
# values += values[:1]
# values

# values2 = rival.iloc[1].tolist()
# values2 += values2[:1]
# values2


# def RadarChart(player, data, player2, data2):
#     Attributes = ['Name', 'Overall', 'Potential', 'SprintSpeed',
#                   'ShotPower', 'ShortPassing', 'Dribbling', 'Stamina', "BallControl"
#                   ]

#     data += data[:1]
#     data2 += data2[:1]

#     angles = [n / 8 * 2 * pi for n in range(8)]
#     angles += angles[:1]

#     angles2 = [n / 8 * 2 * pi for n in range(8)]
#     angles2 += angles2[:1]
#     plt.figure(dpi=125)
#     ax = plt.subplot(111, polar=True)
#     ax = plt.subplot(111, polar=True)

#     plt.xticks(angles[:-1], Attributes)

#     ax.plot(angles, values)
#     ax.fill(angles, values, 'teal', alpha=0.1)

#     ax.plot(angles2, values2)
#     ax.fill(angles2, values2, 'red', alpha=0.1)

#     plt.figtext(0.1, 0.98, player, color="steelblue")
#     plt.figtext(0.1, 0.94, "vs")
#     plt.figtext(0.1, 0.9, player2, color="darkorange")

#     plt.show()


# RadarChart("Messi", [94.0, 94.0, 87.0, 92.0, 92.0, 96.0, 39.0, 66.0], "Ronaldo", [
#            93.0, 93.0, 90.0, 93.0, 82.0, 89.0, 35.0, 78.0])

#################################
# cor = df.corr()

# mask = np.random.rand(len(cor)) < 0.8
# training_data = cor[mask]
# testing_data = cor[~mask]

# print(f"No. of training examples: {training_data.shape[0]}")
# print(f"No. of testing examples: {testing_data.shape[0]}")

# res = sns.heatmap(training_data)
# # res.invert_xaxis()
# res.set_xticklabels(res.get_xmajorticklabels(), fontsize=14)
# res.invert_yaxis()
# res.set_yticklabels(res.get_ymajorticklabels(), fontsize=14)
# plt.show()


# def correlation(dataset, threshold):
#     col_corr = set()  # Set of all the names of correlated columns
#     corr_matrix = dataset.corr()
#     for i in range(len(corr_matrix.columns)):
#         for j in range(i):
#             # we are interested in absolute coeff value
#             if abs(corr_matrix.iloc[i, j] > threshold):
#                 colname = corr_matrix.columns[i]  # getting the name of column
#                 col_corr.add(colname)
#     return col_corr


# corr_features = []
# corr_features = correlation(training_data, 0.999)
# print(corr_features)
# print(len(corr_features))


# corr_featurestest = []
# corr_featurestest = correlation(testing_data, 0.999)
# print(corr_featurestest)
# print(len(corr_featurestest))

# dfnew = df.copy()
# if len(training_data) < len(training_data):
#     for i in corr_features:
#         dfnew.__delitem__(i)
# else:
#     for i in corr_featurestest:
#         dfnew.__delitem__(i)

# print(len(df.transpose()))
# print(len(dfnew.transpose()))
df1 = df[df.columns[10:13]]
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(df1)
principalDf = pd.DataFrame(data=principalComponents, columns=[
                           'principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, df1['CO2EMISSIONS']])
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 component PCA', fontsize=20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['Iris-setosa'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
               finalDf.loc[indicesToKeep, 'principal component 2'], c=color, s=50)
ax.legend(targets)
ax.grid()
