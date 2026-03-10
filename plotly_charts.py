import plotly.express as px
import os


def interactive_scatter(df, x, y):

    fig = px.scatter(df, x=x, y=y, trendline="ols")

    path = f"charts/interactive_scatter_{x}_{y}.html"

    fig.write_html(path)

    print("Saved interactive chart ->", path)


def interactive_line(df, x, y):

    fig = px.line(df, x=x, y=y)

    path = f"charts/interactive_line_{x}_{y}.html"

    fig.write_html(path)

    print("Saved interactive chart ->", path)
