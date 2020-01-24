# Packages
import pandas as pd
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set(style="whitegrid")

import matplotlib as mpl
# label_size = 24
# mpl.rcParams['xtick.labelsize'] = label_size 
# plt.rcParams['xtick.labelsize']=24
# plt.rcParams['ytick.labelsize']=24

import matplotlib.pyplot as plt

SMALL_SIZE = 24
MEDIUM_SIZE = 24
BIGGER_SIZE = 24

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

import wrangle
import linear_random

def get_data():

	# acquire data
	df = pd.read_csv("train_maybe_final.csv")
	df = df[df.world != 'NONE']

	return df

def take_care_double_counts(df):
	clip2 = df.groupby(['installation_id','game_session','world','type','title'])[['event_id']].count()
	clip2 = clip2.drop(columns = 'event_id').reset_index()
	clip2 = clip2.groupby(['installation_id','type'])[['title']].count()
	clip_pivot2 = (clip2
	       .pivot_table(
	           values = 'title', 
	           index = ['installation_id'], 
	           columns = ['type'], 
	           aggfunc=np.sum
	       ).fillna(0).reset_index())
	return clip2, clip_pivot2


def plot_usage(clip2):
	plt.figure(figsize=(16,12))

	c = (clip2.groupby("type")["title"].count())
	pcts = c.groupby(level=0).apply(lambda x: 100 * x / float(c.sum())).to_frame().reset_index()
	#plt.legend(title='Color', loc='center left', bbox_to_anchor=(1, 0.5))
	(sns.barplot(x = "type" , y="title", data=pcts, palette=my_pal))

	plt.title("What are the usage distributions (ratio) for each item in the game?")
	plt.show()


# overall, games and activities are much more used than assessments