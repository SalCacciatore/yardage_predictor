#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import streamlit as st
import random
import numpy as np
import nfl_data_py as nfl
import joblib
from plotly import graph_objects as go


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
# In[4]:


# The following code will apply the NFL yardage predictor model to a web app.


# In[34]:




# In[53]:


#functions

def total_finder(home_or_away,home_total,away_total):
    if home_or_away == 'home':
        total = home_total
    else:
        total = away_total
    return total

def last_name(full):
    if full == 'DanielThomas':
        return 'Thomas'
    elif full == 'JulioJones':
        return 'Jones'
    elif '.' not in full:
        print(full)
        return full
    else:
        return full.split(".",1)[1]

def team_fixer(team):
    if team == 'SD':
        return 'LAC'
    elif team == 'OAK':
        return 'LV'
    elif team == 'STL':
        return 'LA'
    else:
        return team

def name_changer(player):
    if 'Jr.' in player:
        return player.split(' Jr.')[0]
        #return 'D.J. Davis'
    elif 'II' in player:
        return player.split(' II')[0]
    else:
        return player

def position_handler(pos):
    if pos in ['WR','RB','TE','FB']:
        return pos
    elif pos == 'RB/W':
        return 'RB'
    elif pos == 'WR/R':
        return 'WR'
    elif pos == 'HB':
        return 'RB'
    else:
        return 'other'


# In[16]:


import warnings
warnings.filterwarnings('ignore')


# In[128]:


projections = pd.read_csv('trailing_weeks.csv')




# In[130]:



projections = projections.drop_duplicates()

teams = list(projections.reset_index()['posteam'].unique())

players = projections.reset_index()

projections1 = projections.reset_index()[['receiver_player_name','games','pYards','xYards/game','yards/game']].round(1).head(50)

week_by_week = pd.read_csv('weekly_stats.csv')

# In[132]:

def create_scatter(team,answer):
    week_by_week1 = week_by_week[week_by_week['posteam']==team]


    f = week_by_week1.set_index(['receiver_player_name','posteam']).loc[answer][['week','targets','yards_gained','xYards','complete_pass','cp',]]
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=f['week'], y=f['xYards'],name='xYards'))
    fig.add_trace(go.Scatter(x=f['week'], y=f['yards_gained'],name='yards gained'))
    fig.update_layout(title=answer,xaxis_title='Week',yaxis_title='yards')


    st.plotly_chart(fig, use_container_width=True)

header = st.container()

with header:
    st.title("PRO FOOTBALL YARDAGE PREDICTOR")
    st.markdown("Data Source: [nflverse](https://nflverse.nflverse.com/).")
    st.markdown("App and yardage models: Sal Cacciatore")
    st.markdown("Under construction!")







# In[133]:


#weekly_projections = st.container()
#individual = st.container()
test = st.container()


#with weekly_projections:
 #   st.header("Weekly Projections")
 #   ldr = st.form(key = '2022')
 #   ldr_submitted = ldr.form_submit_button("Click here for this week's yardage projections.")
 #   st.markdown("Leaderboard assumes the player is not injured or on a bye.")
 #   if ldr_submitted:
 #       st.table(data=projections1)


#with individual:
 #   st.header("Player Projections")
 #   st.markdown("Look at a player's projections for this week.")
 #   sel_col, disp_col = st.columns(2)

    #form = st.form(key = "player_selection")
 #   player_prompt = sel_col.selectbox("Select a team.",options=teams)
 #   df = players[players['posteam']==player_prompt]
 #   recs = list(df['receiver_player_name'].unique())
 #   proj_prompt = sel_col.selectbox("Select a player.",options=recs)
 #   current_form = st.form(key='current_selection')
 #   t_submitted = current_form.form_submit_button("Submit")
 #   if t_submitted:
 #       tm = df[df['receiver_player_name']==proj_prompt]
 #       st.table(data=tm[['receiver_player_name','posteam','games','pYards','xYards/game','yards/game']].set_index('receiver_player_name'))
 #       create_scatter(player_prompt, proj_prompt)


with test:
    st.header("Widget Test")
    def what_chart(what_chart_do_you_want):
        return what_chart_do_you_want

    
    ichart=interactive(what_chart, what_chart_do_you_want=['LAST 7 DAYS','CUSTOM DATE RANGE','CUMULATIVE PROFIT'])
    display(ichart)

 #   sel_col, disp_col = st.columns(2)



# In[ ]:





# In[ ]:
