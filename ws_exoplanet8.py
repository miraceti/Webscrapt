import plotly.express as px
import pandas as pd

df = px.data.gapminder()
print(df)

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    size="pop",
    hover_name="country",
    log_x=True,
    size_max=60,
)

fig.show()


