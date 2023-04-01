import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits import mplot3d

def activity(s):
    if s[0] == '<':
        if float(s[1:]) <= 1:
            return 1
        else:
            return np.nan
    elif s[0] == '>':
        if float(s[1:]) >= 1:
            return 0
        else:
            return np.nan
    else:
        if float(s) > 1:
            return 0
        else:
            return 1

data = pd.read_csv('../data/SHP2_train_descriptors_2741.csv')
data['TARGET'] = data['IC50(microM)'].apply(activity)
data = data.dropna()
z = data['MolMR'].values
x = data['MolWt'].values
y = data['MolLogP'].values
labels = data['TARGET'].values

# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.3,
        alpha = 0.2)

# Creating plot
sctt = ax.scatter3D(xs=x, ys=y, zs=z, c=labels, s=5, cmap = 'RdYlGn')
plt.title("Chemical Space")
ax.set_xlabel('MolWt', fontweight ='bold')
ax.set_ylabel('MolLogP', fontweight ='bold')
ax.set_zlabel('MolMR', fontweight ='bold')
#ax.view_init(-140, 0)
fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 10, use_gridspec=False)
ax.legend()
# show plot
plt.show()