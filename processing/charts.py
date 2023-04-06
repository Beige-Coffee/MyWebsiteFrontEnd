import plotly.graph_objects as go
import streamlit as st

def display_pie_chart(pool_data, width=600, height=400):
    # Extract pool names and the number of blocks mined
    pool_names = list(pool_data.keys())
    blocks_mined = list(pool_data.values())

    # Create a pie chart using Plotly
    fig = go.Figure(
        go.Pie(
            labels=pool_names,
            values=blocks_mined,
            hoverinfo="label+percent",
            textinfo="label+percent",
            textfont=dict(size=10)  # Adjust font size if needed
            #marker=dict(colors=custom_bitcoin_orange_colors, line=dict(color="#000000", width=0.5))
            #marker=dict(colors=custom_bitcoin_orange_colors, line=dict(color="#000000", width=0.5))
        )
    )

    # Set the size of the pie chart
    fig.update_layout(width=width, height=height)

    # Display the pie chart in Streamlit
    st.plotly_chart(fig)


def build_bitcoin_summary(data):

    with st.expander("View Network Summary Data"):
            
        # Create four columns
        col1, col2, col3, col4 = st.columns([2,2,2,2])

        # Display content in the second column
        with col1:

            st.write("<b style='font-size: 24px;'>Summary</b>",
                        unsafe_allow_html=True)
            st.write(f"Market Price (USD): {data['market_price_usd']}", style='font-size: smaller;')
            st.write(f"Hash Rate: {data['hash_rate']}", style='font-size: smaller;')
            st.write(f"Difficulty: {data['difficulty']}", style='font-size: smaller;')

        with col2:

            #st.subheader("Block Information (Last 24h)")
            st.write("<b style='font-size: 24px;'>Block Information (Last 24h)</b>",
                        unsafe_allow_html=True)
            st.write(f"Number of Blocks Mined: {data['n_blocks_mined']}", style='font-size: smaller;')
            st.write(f"Total Number of Blocks: {data['n_blocks_total']}", style='font-size: smaller;')
            st.write(f"Next Retarget: {data['nextretarget']}", style='font-size: smaller;')
            st.write(f"Minutes Between Blocks: {data['minutes_between_blocks']}", style='font-size: smaller;')
        
        with col3:

            #st.subheader("Transaction Information (Last 24h)")
            st.write("<b style='font-size: 24px;'>Transaction Information (Last 24h)</b>",
                        unsafe_allow_html=True)
            st.write(f"Number of Transactions: {data['n_tx']}", style='font-size: smaller;')
            st.write(f"Estimated BTC Sent: {data['estimated_btc_sent']}", style='font-size: smaller;')
            st.write(f"Total BTC Sent: {data['total_btc_sent']}", style='font-size: smaller;')

        with col4:
            #st.subheader("Trade Volume (Last 24h)")
            st.write("<b style='font-size: 24px;'>Trade Volume (Last 24h)</b>",
                        unsafe_allow_html=True)
            st.write(f"Trade Volume (BTC): {data['trade_volume_btc']}", style='font-size: smaller;')
            st.write(f"Trade Volume (USD): {data['trade_volume_usd']}", style='font-size: smaller;')