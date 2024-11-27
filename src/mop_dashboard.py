import pandas as pd
import streamlit as st
import json
import os
import sys
import plotly.graph_objects as go

sys.path.append(os.path.dirname(os.path.dirname("..")))
from definitions import ROOT_DIR


def get_status_color(status):
    if status.split("-")[0] == "4":
        # return 'rgb(43,177,218)'
        return "rgb(0,158,213)"
    if status.split("-")[0] == "3":
        return "rgb(0,138,206)"
    elif status.split("-")[0] == "2":
        return "rgb(0,118,198)"
    elif status.split("-")[0] == "1":
        return "rgb(8,97,186)"
    elif status.split("-")[0] == "5":
        return "gray"
    else:
        return "gray"


def get_status_text(status):
    if status.split("-")[0] == "1":
        return "Adjudicación"
    if status.split("-")[0] == "2":
        return "Operación"
    elif status.split("-")[0] == "3":
        return "Construcción"
    elif status.split("-")[0] == "4":
        return "Construcción y Operación"
    elif status.split("-")[0] == "5":
        return "Finalizada"
    else:
        return "Desconocido"


def set_page_config():
    st.set_page_config(
        page_title="Estado de las concesiones",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    hide_default_format = """
       <style>
       MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       .reportview-container .main .block-container .stMain{
        padding-top: 0rem;
        margin-top: 0rem;
       }
       .modebar{
      display: none !important;
}
       </style>
       """
    st.markdown(hide_default_format, unsafe_allow_html=True)


def load_data():
    # open the json file
    with open(ROOT_DIR + "/data/mop_details_clean.json", "r") as f:
        data = json.load(f)

    return data


def statuses_bar_chart(df):
    ##Start of status horizontal bar chart
    values_list = df["status"].value_counts()
    values_list = values_list.sort_index()

    fig = go.Figure()

    for label, value in values_list.items():
        fig.add_trace(
            go.Bar(
                y=["count"],
                x=[value],
                orientation="h",
                name=label,
                text=[f"{get_status_text(label)} ({value})"],
                textangle=270,
                textposition="inside",
                textfont_color="rgb(255,255,255)",
                marker_color=get_status_color(label),
                marker_line_width=0.5,
                marker_line_color="rgb(255,255,255)",
                hoverinfo="text",
                hoverlabel=dict(
                    bgcolor=get_status_color(label), font_color="rgb(255,255,255)"
                ),
            )
        )

    (
        fig.update_layout(
            margin=dict(t=0, b=0),
            height=200,
            barmode="stack",
            showlegend=False,
            yaxis={"visible": False, "showticklabels": False},
            xaxis={
                "visible": False,
                "showticklabels": False,
            },
            title_text="Estado de las concesiones",
        ),
    )


data = load_data()
df = pd.DataFrame(data)

set_page_config()

status, xx, yy = st.columns([2, 1, 1], gap="large", vertical_alignment="bottom")
with status:
    statuses_bar_chart(df)
with xx:
    st.write("")
with yy:
    st.write("")


st.write(df)
