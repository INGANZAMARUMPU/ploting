import pandas as pd
import plotly
import plotly.graph_objs as go

#Read cars data from csv
data = pd.read_csv("tensile.csv")

#Set marker properties
marker_size = data['Fe']/5
marker_color = data['S']*100
# marker_opacity = data['P']*10

#==============================================================================
#Make Plotly figure
elasticite = go.Scatter3d(x=data['C'],
                    y=data['Si'],
                    z=data['elasticite'],
                    marker=dict(size=marker_size,
                                color=marker_color,
                                # opacity=marker_opacity,
                                opacity=0.9,
                                reversescale=True,
                                colorscale='Reds'),

                    line=dict (width=0.02),
                    mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict( title="C"),
                                yaxis=dict( title="Si"),
                                zaxis=dict(title="elasticite")),)
#Plot and save html
plotly.offline.plot({"data": [elasticite],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("elasticite.html"))

#==============================================================================

#Make Plotly figure
traction = go.Scatter3d(x=data['C'],
                    y=data['Si'],
                    z=data['traction'],
                    marker=dict(size=marker_size,
                                color=marker_color,
                                # opacity=marker_opacity,
                                opacity=0.9,
                                reversescale=True,
                                colorscale='Reds'),

                    line=dict (width=0.02),
                    mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict( title="C"),
                                yaxis=dict( title="Si"),
                                zaxis=dict(title="traction")),)
#Plot and save html
plotly.offline.plot({"data": [traction],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("traction.html"))

#==============================================================================

#Make Plotly figure
plasticite = go.Scatter3d(x=data['C'],
                    y=data['Si'],
                    z=data['plasticite'],
                    marker=dict(size=marker_size,
                                color=marker_color,
                                # opacity=marker_opacity,
                                opacity=0.9,
                                reversescale=True,
                                colorscale='Reds'),

                    line=dict (width=0.02),
                    mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict( title="C"),
                                yaxis=dict( title="Si"),
                                zaxis=dict(title="plasticite")),)
#Plot and save html
plotly.offline.plot({"data": [plasticite],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("plasticite.html"))

#==============================================================================
#Make Plotly figure
resistance_chocs = go.Scatter3d(x=data['C'],
                    y=data['Si'],
                    z=data['resistance_chocs'],
                    marker=dict(size=marker_size,
                                color=marker_color,
                                # opacity=marker_opacity,
                                opacity=0.9,
                                reversescale=True,
                                colorscale='Reds'),

                    line=dict (width=0.02),
                    mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict( title="C"),
                                yaxis=dict( title="Si"),
                                zaxis=dict(title="resistance_chocs")),)
#Plot and save html
plotly.offline.plot({"data": [resistance_chocs],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("resistance_chocs.html"))

