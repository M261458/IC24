import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

nutrient_df = pd.read_csv('nutrient_stdev_diff.csv')
print(nutrient_df)

fig = px.bar(nutrient_df, x="SR_Component", y="stdev_difference", color="SR Food description", barmode="group")
fig.show()

# fig = go.Figure()
# for Food, group in nutrient_df.groupby("SR Food description"):
#     fig.add_trace(go.Bar(x=group["SR_Component"], y=group["stdev_difference"], name=Food,
#       hovertemplate="SR Food description=%s<br>SR_Component=%%{x}<br>stdev_difference=%%{y}<extra></extra>"% Food))
# fig.update_layout(legend_title_text = "SR Food description")
# fig.update_xaxes(title_text="stdev_difference")
# fig.update_yaxes(title_text="Stdev Error")
# fig.show()