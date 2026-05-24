import streamlit as st
import pandas as pd
import plotly.express as px

from Profiler.Data_Profiler import generate_profile

st.set_page_config(page_title="AI Data Profiling Agent")

st.title("AI Data Profiling Agent")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success("File Uploaded Successfully")

    # Dataset preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Generate profile
    profile = generate_profile(df)

    # Dataset summary
    st.subheader("Dataset Summary")

    st.write(f"Rows: {profile['rows']}")
    st.write(f"Columns: {profile['columns']}")
    st.write(f"Duplicate Rows: {profile['duplicate_rows']}")

    # Better column analysis table
    st.subheader("Column Analysis")

    column_df = pd.DataFrame({
        "Column": profile["column_names"],
        "Data Type": [
            profile["dtypes"][col]
            for col in profile["column_names"]
        ],
        "Null %": [
            profile["null_percentages"][col]
            for col in profile["column_names"]
        ],
        "Unique Values": [
            profile["unique_counts"][col]
            for col in profile["column_names"]
        ]
    })

    st.dataframe(column_df)
    
    # Null percentage chart
    st.subheader("Null Percentage Analysis")
    
    fig = px.bar(
     column_df,
     x="Column",
     y="Null %",
     title="Null Percentage by Column",
     text="Null %"
    )

# Force Y-axis from 0 to 100
    fig.update_yaxes(range=[0, 100])

# Better layout
    fig.update_layout(
     xaxis_title="Columns",
     yaxis_title="Null Percentage (%)"
    )

# Show labels on bars
    fig.update_traces(textposition="outside")

    st.plotly_chart(fig)