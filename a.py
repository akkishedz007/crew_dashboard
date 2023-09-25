import pandas as pd
import numpy as py

import streamlit as st
import plotly.express as px

df = pd.read_csv('consolidated_data.csv')
df.shape
df.columns
df.head(10)
df.dtypes
crew= df.copy()
crew[crew.duplicated()].shape
crew[crew.duplicated()]
crew_cleaned1=crew.drop_duplicates()
import seaborn as sns
cols = crew_cleaned1.columns 
colours = ['#000099', '#ffff00'] # specify the colours - yellow is missing. blue is not missing.
sns.heatmap(crew_cleaned1[cols].isnull(),
            cmap=sns.color_palette(colours))
crew_cleaned1[crew_cleaned1.isnull().any(axis=1)].head()
crew_cleaned1.isnull().sum()
import sweetviz as sv
sweet_report = sv.analyze(crew_cleaned1)
sweet_report.show_html('crew_dashboard.html')
