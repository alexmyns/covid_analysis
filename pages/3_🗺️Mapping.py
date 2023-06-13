import streamlit as st
import plotly.express as px
from Home import from_data

# color pallette
cnf, dth, rec, act = '#393e46', '#ff2e63', '#21bf73', '#fe9801'

def mapping_demo():
    from urllib.error import URLError

    st.markdown(f"# ")
    data = from_data()
    try:
        def plot_map(df, col, pal = '#393e46'):
            col1 = df[df[col[0]] > 0]
            col2 = df[df[col[1]] > 0]
            fig1 = px.choropleth(col1, locations="Country/Region", locationmode='country names',
                                color=col[0], hover_name="Country/Region",
                                title=col[0], hover_data=[col[0]], color_continuous_scale=pal)

            fig2 = px.choropleth(col2, locations="Country/Region", locationmode='country names',
                                color=col[1], hover_name="Country/Region",
                                title=col[1], hover_data=[col[1]], color_continuous_scale=pal)
            #     fig.update_layout(coloraxis_showscale=False)

            tab1, tab2, tab3 = st.tabs(["Active Cases", "Deaths/1M pop", "TreeMap All"])
            with tab1:
                # Use the Streamlit theme.
                # This is the default. So you can also omit the theme argument.
                st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
            with tab2:
                # Use the native Plotly theme.
                st.plotly_chart(fig2, theme=None, use_container_width=True)
            with tab3:
                temp = df[['WHO Region', 'ActiveCases', 'Deaths/1M pop', 'NewRecovered']]
                temp = temp.melt(id_vars='WHO Region', value_vars=['ActiveCases', 'Deaths/1M pop', 'NewRecovered'])
                fig3 = px.treemap(temp, path=["variable"], values="value", height=225,
                                 color_discrete_sequence=[act, rec, dth])
                fig3.data[0].textinfo = 'label+text+value'
                st.plotly_chart(fig3, theme="streamlit", use_container_width=True)

        plot_map(data, ['ActiveCases', 'Deaths/1M pop'], 'matter')
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )
if __name__ == '__main__':
    mapping_demo()