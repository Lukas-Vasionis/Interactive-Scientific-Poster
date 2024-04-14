import streamlit as st


def multiselect_circles():
    circle_options = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
    all = st.checkbox("Select all circles", value=True)
    if all:
        selection_circles = st.multiselect("Filter: Circles of Hell:",
                                           circle_options, circle_options)
    else:
        selection_circles = st.multiselect("Filter: Circles of Hell:",
                                           circle_options)
    return selection_circles


def radio_energy_barplot_mode():
    bar_mode = st.radio(label='Energy outputs in:',
                        options=['Units (Infernals)','Percents'])
    return bar_mode

def slider_measurement_day(heatmap_data):
    slider=st.select_slider("Population measurement day",
                     options=range(1, len(heatmap_data) + 1), value=1)
    return slider