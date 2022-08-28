# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html


external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = dash.Dash(
    __name__,
    external_scripts=external_script,
)
app.scripts.config.serve_locally = True

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame(
    {
        "Sensor": ["001", "002", "003", "004", "005", "006"],
        "Speed": [4.2, 1.0, 2.1, 2.32, 4.20, 5.0],
    }
)


sensor_count = df.Sensor.count()
avr_speed = int(df.Speed.sum() / sensor_count)
active_sensors = 4
inactive_sensors = 2

fig = px.bar(df, x="Sensor", y="Speed",)

app.layout = html.Div(
    html.Div(
        children=[
            html.Div(
                children=[
                    html.H1(children="DKU Gym Sensors Dashboard", className=" py-3 text-5xl font-bold text-gray-800"),
                    html.Div(
                        children="""
                                """,
                        className="text-left prose prose-lg text-2xl  py-3 text-gray-600",
                    ),
                ],
                className="w-full mx-14 px-16 shadow-lg bg-white -mt-14 px-6 container my-3 ",
            ),
            html.Div(
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                f"{sensor_count}",
                                html.Br(),
                                html.Span("Total # of Sensors", className="text-lg font-bold ml-4"),
                            ],
                            className=" shadow-xl py-3 px-12 text-5xl bg-[#1d3557] text-white text-center font-bold text-gray-800",
                        ),
                        html.Div(
                            children=[
                                active_sensors,
                                html.Br(),
                                html.Span("Active", className="text-lg font-bold ml-4"),
                            ],
                            className=" shadow-xl py-3 px-12 text-5xl bg-[#76c893] text-white text-center font-bold text-gray-800",
                        ),
                        html.Div(
                            children=[
                                inactive_sensors,
                                html.Br(),
                                html.Span("Inactive", className="inline-flex items-center text-lg font-bold"),
                            ],
                            className=" shadow-xl py-3 px-12 text-5xl bg-[red] text-white text-center font-bold text-gray-800",
                        ),
                        html.Div(
                            children=[
                                avr_speed,
                                html.Br(),
                                html.Span("Average Speed", className="inline-flex items-center text-lg font-bold"),
                            ],
                            className=" shadow-xl py-3 px-12 text-5xl bg-[#646ffa] text-white text-center font-bold text-gray-800",
                        ),
                        
                    ],
                    className="my-4 w-full grid grid-flow-rows grid-cols-1 lg:grid-cols-4 gap-y-4 lg:gap-[60px]",
                ),
                className="flex max-w-full justify-between items-center ",
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Img(src="../assets/gym_photo.png", alt="gym photo"),
                            html.Div()
                        ],
                        className="bg-white",
                    ),
                    html.Div(
                        children=[
                            dcc.Graph(id="example-graph2", figure=fig),
                        ],
                        className="w-full shadow-2xl rounded-sm",
                    ),
                ],
                className="grid grid-cols-1 lg:grid-cols-2 gap-4",
            ),
        ],
        className="bg-[#ebeaee]  flex py-14 flex-col items-center justify-center ",
    ),
    className="bg-[#ebeaee] container mx-auto px-14 py-4",
)

if __name__ == "__main__":
    app.run_server(debug=True)