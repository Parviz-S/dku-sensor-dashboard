# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash_iconify import DashIconify

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

fig = px.bar(df, x="Sensor", y="Speed", )


def generate_infocard(text, data, change):
    return html.Div(
        children=[
            html.Div([
                html.Div(html.Span(text, className="text-[14px] font-bold text-[#A2AAAD]")),
                html.Div(html.Span(f"{data}", className="counter text-[28px] font-light")),
                html.Div(html.Span(f"Learn More", className="link text-[12px] border-b-2 border-gray")),
            ], className="left flex flex-col justify-between"),
            html.Div([
                html.Div([
                    DashIconify(
                        icon="bi:arrow-up-right-square-fill",
                        width=20,
                    ),
                    html.Span(f"{change}", className="percentage positive text-[14px] pl-[5px]")
                ], className="flex"),
                html.Div(DashIconify(
                    icon="bi:bar-chart-fill",
                    width=30,
                ), className="self-end"),
            ], className="right left flex flex-col justify-between"),
        ],
        className=f"flex flex-1 p-[10px] h-[120px] justify-between shadow-lg rounded-lg",
    )


app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[html.Span(children="Smart Sensor Dashboard",
                                        className="logo font-[20px] font-bold text-[#6439ff]")],
                    className="top h-[50px] flex items-center justify-center"
                ),
                html.Hr(className="h-[0px] border-[0.5px] border-[lightgray]"),
                html.Div(
                    children=html.Ul(children=[
                        html.Li(children=[
                            html.Span(children="Sensors"),
                        ]),
                        html.Li(children=[
                            html.Span(children="Sensors"),
                        ]),
                        html.Li(children=[
                            html.Span(children="Sensors"),
                        ]),
                    ]),
                    className="center pl-10"
                ),
                html.Div(
                    children="color options",
                    className="bottom"
                )
            ],
            className="sidebar bg-white basis-1/6 border-r-[0.5px] border-[lightgray] min-h-[100vh]"
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.Div("About", className="pl-2 pr-1"),
                                html.Div("Team", className="pl-2 pr-1"),
                                html.Div("Contact Us", className="pl-2 pr-1"),
                            ],
                            className="wrapper flex w-[100%] justify-end"
                        )
                    ],
                    className="navbar h-[50px] flex items-center font-[14px] text-[#555]"
                ),
                html.Hr(className="h-[0px] border-[0.5px] border-[lightgray]"),
                html.Div(
                    children=[
                        generate_infocard("TOTAL SENSORS", sensor_count, "20%", ),
                        generate_infocard("ACTIVE", active_sensors, "20%", ),
                        generate_infocard("INACTIVE", inactive_sensors, "20%", ),
                        generate_infocard("AVERAGE SPEED", avr_speed, "20%", ),
                    ],
                    className="flex p-[20px] gap-[20px]",
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
            className="bg-white basis-5/6",
        ),
    ],
    className="flex",
)

if __name__ == "__main__":
    app.run_server(debug=True)
