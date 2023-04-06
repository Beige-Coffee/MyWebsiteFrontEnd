import streamlit as st
import qrcode
import requests
import tempfile
import os
import pandas as pd


def tip():

    st.text("Create Lightning Invoice")

    with st.form(key="invoice_form"):
        satoshis = st.number_input("Amount (in Satoshis)", min_value=1, step=1, value=1000)
        memo = st.text_input("Invoice Memo")
        submit_button = st.form_submit_button("Create Invoice")

    if submit_button:

        data = {
            "amount" : satoshis,
            "memo": memo
            }

        url = "http://127.0.0.1:8000/invoice"

        response = requests.post(url, json=data)

        invoice = response.json()['request']

        img = qrcode.make(invoice)

        img_file_path = os.path.join("static", "images", "invoice.png")

        img.save(img_file_path)

        st.image(img_file_path, width=200)

        # Process the input data and create the Lightning invoice
        st.success(f"Lightning Invoice created for {satoshis} satoshis with memo: {memo}")
        # You can replace the above line with your logic for creating the Lightning invoice using the provided amount and memo.

    
    url = "http://127.0.0.1:8000/invoice"
    invoices = requests.get(url).json()['invoices']
    df = pd.DataFrame(invoices)
    st.dataframe(df)


    


    