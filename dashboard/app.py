import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import os

st.set_page_config(page_title="AI Finance Analyzer", layout="wide")

st.title("AI Personal Finance Analyzer & Spending Predictor")
st.write("Upload your transaction CSV file to analyze spending and predict future expenses.")

uploaded_file = st.file_uploader("Upload your transaction CSV", type=["csv"])


def generate_insights(df):

    insights = []

    total_spending = df["Amount"].sum()
    insights.append(f"Total spending is ₹{round(total_spending,2)}")

    category_spending = df.groupby("Category")["Amount"].sum()
    top_category = category_spending.idxmax()
    insights.append(f"Highest spending category is {top_category}")

    df["Date"] = pd.to_datetime(df["Date"])
    df["Day"] = df["Date"].dt.day_name()

    weekend_spending = df[df["Day"].isin(["Saturday","Sunday"])]["Amount"].sum()
    weekday_spending = df[~df["Day"].isin(["Saturday","Sunday"])]["Amount"].sum()

    if weekend_spending > weekday_spending:
        insights.append("You spend more money on weekends.")
    else:
        insights.append("You spend more money on weekdays.")

    return insights


if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Transaction Data")
    st.dataframe(df.head())

    st.subheader("Total Spending")
    st.metric("Total Amount", f"₹{round(df['Amount'].sum(),2)}")

    st.subheader("Spending by Category")

    category_spending = df.groupby("Category")["Amount"].sum()
    st.bar_chart(category_spending)

    st.subheader("Payment Mode Distribution")

    payment_spending = df.groupby("Payment_Mode")["Amount"].sum()

    fig, ax = plt.subplots()
    ax.pie(payment_spending, labels=payment_spending.index, autopct='%1.1f%%')
    st.pyplot(fig)

    st.subheader("AI Spending Insights")

    insights = generate_insights(df)

    for insight in insights:
        st.write("•", insight)

        