import pandas as pd
import plotly.graph_objects as go

df2 = pd.read_csv("~/Downloads/stock_details_5_years.csv")
print(df2.head())
print(df2.shape)
df2['Date'] = pd.to_datetime(df2['Date'])
print(df2['Date'].min())
print(df2['Date'].max())

df2_filtrat = df2[
    (df2['Company'] == 'GOOGL') &
    (df2['Date'] >= pd.Timestamp('2023-01-01 00:00:00-05:00')) &
    (df2['Date'] <= pd.Timestamp('2023-06-01 00:00:00-05:00'))
]

print(df2_filtrat.head())
print(df2_filtrat.shape)
print(df2_filtrat.columns)

fig = go.Figure(data=go.Ohlc(x=df2_filtrat['Date'],
                             open=df2_filtrat['Open'],
                             high=df2_filtrat['High'],
                             low=df2_filtrat['Low'],
                             close=df2_filtrat['Close']))

fig.update_layout(
    title={
        'text':'Evolució del preu de les accions de Google',
        'x': 0.5,
        'font': {
            'size': 30
        }
    },
    yaxis_title ={
        'text':'Preu',
        'font': {
            'size':20
        }
    }
