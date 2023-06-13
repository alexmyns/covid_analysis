import streamlit as st
import numpy as np
import plotly.express as px
import time

from Home import from_data

# color pallette
cnf, dth, rec, act = '#393e46', '#ff2e63', '#21bf73', '#fe9801'

def plotting_demo():
    # Using object notation
    add_selectbox = st.sidebar.selectbox(
        "Choose graphs",
        ("Bars", "Scatters", "Treemaps")
    )

    st.markdown(f'# s')
    st.write(
        """
        This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!
"""
    )
    df = from_data()
    def plot_hbar(df, col, n, hover_data=[]):
        fig = px.bar(df.sort_values(col, ascending=False).head(n),
                     x=col, y="Country/Region", color='WHO Region',
                     text=col, orientation='h', width=700, hover_data=hover_data,
                     color_discrete_sequence=px.colors.qualitative.Dark2)
        fig.update_layout(title=col, xaxis_title="", yaxis_title="",
                          yaxis_categoryorder='total ascending',
                          uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig, use_container_width=True)

    def plot_hbar_wm(df, col, n, min_pop=1000000, sort='descending'):
        df = df[df['Population'] > min_pop]
        df = df.sort_values(col, ascending=True).head(n)
        fig = px.bar(df,
                     x=col, y="Country/Region", color='WHO Region',
                     text=col, orientation='h', width=700,
                     color_discrete_sequence=px.colors.qualitative.Dark2)
        fig.update_layout(title=col + ' (Only countries with > 1M Pop)',
                          xaxis_title="", yaxis_title="",
                          yaxis_categoryorder='total ascending',
                          uniformtext_minsize=8, uniformtext_mode='hide')
        st.plotly_chart(fig, use_container_width=True)

    def scatter_plots(df):
        fig = px.scatter(df.sort_values('TotalCases', ascending=False).iloc[:10, :],
                         x='TotalCases', y='Deaths/1M pop', color='Country/Region', size='TotalCases',
                         height=700, text='Country/Region', log_x=True, log_y=True,
                         title='Deaths vs TotalCases (Scale is in log10)')
        fig.update_traces(textposition='top center')
        fig.update_layout(showlegend=False)
        fig.update_layout(xaxis_rangeslider_visible=True)
        st.plotly_chart(fig, use_container_width=True)

    def plot_treemap(df, col):
        fig = px.treemap(df, path=["Country/Region"], values=col, height=700,
                         title=col, color_discrete_sequence=px.colors.qualitative.Dark2)
        fig.data[0].textinfo = 'label+text+value'
        st.plotly_chart(fig, use_container_width=True)


    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.02)

    if add_selectbox == 'Bars':
        col1, col2 = st.columns([1, 1])
        with col1:
            plot_hbar(df, 'TotalCases', 15)
        with col2:
            plot_hbar(df, 'ActiveCases', 15)

        col1, col2 = st.columns([1, 1])
        with col1:
            plot_hbar_wm(df, 'Tests/1M pop', 15)
        with col2:
            plot_hbar_wm(df, 'Tot Cases/1M pop', 15)

    if add_selectbox == 'Scatters':
        tab1, tab2 = st.tabs(['Deaths vs TotalCases (Scale is in log10)', 'Active vs Cured (Scale is in log10)'])
        with tab1:
            scatter_plots(df)
        with tab2:
            scatter_plots(df)
    if add_selectbox == 'Treemaps':
        tab1, tab2 = st.tabs(['ActiveCases', 'Deaths/1M pop'])

        with tab1:
            plot_treemap(df, 'ActiveCases')
        with tab2:
            plot_treemap(df, 'Deaths/1M pop')
    progress_bar.empty()



    # rerun.
    st.button("Re-run")

if __name__ == '__main__':
    plotting_demo()