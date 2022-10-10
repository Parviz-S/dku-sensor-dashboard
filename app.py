# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import pandas as pd
import plotly.express as px
import numpy as np
from dash import dcc, html
from dash_iconify import DashIconify

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

sample_data = pd.read_csv("sample_data.csv")
sample_data.drop('Unnamed: 0', inplace=True, axis=1)
sample_data['epoch'] = pd.to_datetime(sample_data['epoch'], unit='ms')
print(sample_data)

# data = pd.DataFrame(data)
# print(data)
# data = data[[0, 3, 6, 9]]
# data = data.rename(columns={0: 'epoch', 3: 'x', 6: 'y', 9: 'z'})


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

# fig = px.bar(df, x="Sensor", y="Speed", )
fig = px.line(sample_data, x="epoch", y=["x", "y", "z"], title="Selected: Sensor 1 (active)")
fig_extra = px.line(sample_data, x="epoch", y=["x", "y", "z"], title="Sensor # (active/inactive)")


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
                                        className="logo font-[20px] font-bold text-blue-700")],
                    className="top h-[50px] flex items-center justify-center"
                ),
                html.Hr(className="h-[0px] border-[0.5px] border-[lightgray]"),
                html.Div([
                    html.A("Sensor 1", className="block py-2 px-4 w-full text-white bg-blue-700 rounded-t-lg border-b "
                                                 "border-gray-200 cursor-pointer"),
                    html.A("Sensor 2", className="block py-2 px-4 w-full border-b border-gray-200 cursor-pointer "
                                                 "hover:bg-gray-100 hover:text-blue-700 focus:outline-none "
                                                 "focus:ring-2 focus:ring-blue-700 focus:text-blue-700"),
                    html.A("Sensor 3", className="block py-2 px-4 w-full border-b border-gray-200 cursor-pointer "
                                                 "hover:bg-gray-100 hover:text-blue-700 focus:outline-none "
                                                 "focus:ring-2 focus:ring-blue-700 focus:text-blue-700"),
                    html.A("Sensor 4", className="block py-2 px-4 w-full border-b border-gray-200 cursor-pointer "
                                                 "hover:bg-gray-100 hover:text-blue-700 focus:outline-none "
                                                 "focus:ring-2 focus:ring-blue-700 focus:text-blue-700"),
                    html.A("Sensor 5", className="block py-2 px-4 w-full border-b border-gray-200 cursor-pointer "
                                                 "hover:bg-gray-100 hover:text-blue-700 focus:outline-none "
                                                 "focus:ring-2 focus:ring-blue-700 focus:text-blue-700"),
                    html.A("Sensor 6", className="block py-2 px-4 w-full rounded-b-lg cursor-pointer "
                                                 "hover:bg-gray-100 hover:text-blue-700 focus:outline-none "
                                                 "focus:ring-2 focus:ring-blue-700 focus:text-blue-700"),

                ], className="ml-[5%] mt-[15px] w-[90%] justify-center text-sm font-medium text-gray-900 bg-white "
                             "rounded-lg border border-gray-200"),
            ],
            className="sidebar bg-white basis-1/6 border-r-[0.5px] border-[lightgray] min-h-[100vh]"
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.A("Project Site (CDL)", href="/", className="pl-2 pr-1"),
                                html.A("Project Repo", href="https://github.com/Parviz-S/dku-sensor-dashboard",
                                       className="pl-2 pr-1"),
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
                                html.Div("Map of the Sensors", className="text-lg mb-[10px] mt-[10px] text-center"),
                                html.Img(src="../assets/gym_photo.png", alt="gym photo"),
                            ],
                            className="bg-white w-full shadow-2xl rounded-sm",
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(id="selected_graph", figure=fig),
                            ],
                            className="w-full shadow-2xl rounded-sm",
                        ),
                    ],
                    className="grid grid-cols-1 lg:grid-cols-2 gap-4 ml-[1%] mr-[1%]",
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dcc.Graph(id="example_graph1", figure=fig_extra),
                            ],
                            className="w-full shadow-2xl rounded-lg",
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(id="example_graph2", figure=fig_extra),
                            ],
                            className="w-full shadow-2xl rounded-lg",
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(id="example_graph3", figure=fig_extra),
                            ],
                            className="w-full shadow-2xl rounded-lg",
                        ),
                    ],
                    className="grid grid-cols-1 lg:grid-cols-3 gap-4 ml-[1%] mr-[1%] mt-[15px]",
                ),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dcc.Graph(id="example_graph4", figure=fig_extra),
                            ],
                            className="w-full shadow-2xl rounded-lg",
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(id="example_graph5", figure=fig_extra),
                            ],
                            className="w-full shadow-2xl rounded-lg",
                        ),
                        html.Div(
                            children=[
                                dcc.Graph(id="example_graph6", figure=fig_extra),
                            ],
                            className="w-full shadow-2xl rounded-lg",
                        ),
                    ],
                    className="grid grid-cols-1 lg:grid-cols-3 gap-4 ml-[1%] mr-[1%] mt-[15px]",
                ),
            ],
            className="bg-white basis-5/6",
        ),
    ],
    className="flex",
)
if __name__ == "__main__":
    app.run_server(debug=True)
