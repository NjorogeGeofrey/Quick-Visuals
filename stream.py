import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Custom CSS for styling
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f5f5f5;
        padding: 10px;
    }
    .sidebar .scatter-section {
        background-color: #e6f7ff;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    .sidebar .pie-section {
        background-color: #fff2e6;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    .sidebar .line-section {
        background-color: #e6ffe6;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    .sidebar .bar-section {
        background-color: #fff5e6;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    .sidebar .histogram-section {
        background-color: #ffe6f7;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Quick Visuals Dashboard")
st.sidebar.title("Navigation")

uploaded_file = st.sidebar.file_uploader("Upload your csv or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    st.write("### Data Preview")
    st.dataframe(df)

    st.write("### Basic Statistics")
    st.write(df.describe())

    st.sidebar.subheader("Select Visualization")

    visualization_type = st.sidebar.selectbox(
        "Choose the type of visualization",
        ["Scatter Plot", "Pie Chart", "Line Chart", "Bar Chart", "Histogram"]
    )

    columns = df.columns.tolist()

    if visualization_type == "Scatter Plot":
        st.sidebar.markdown('<div class="scatter-section">', unsafe_allow_html=True)
        x_axis_scatter = st.sidebar.selectbox("X-Axis for Scatter Plot", columns, key='scatter_x')
        y_axis_scatter = st.sidebar.selectbox("Y-Axis for Scatter Plot", columns, key='scatter_y')
        st.sidebar.markdown('</div>', unsafe_allow_html=True)

        if x_axis_scatter and y_axis_scatter:
            st.write("### Scatter Plot")
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[x_axis_scatter], y=df[y_axis_scatter], ax=ax)
            ax.set_xlabel(x_axis_scatter)
            ax.set_ylabel(y_axis_scatter)
            st.pyplot(fig)

    elif visualization_type == "Pie Chart":
        st.sidebar.markdown('<div class="pie-section">', unsafe_allow_html=True)
        pie_column = st.sidebar.selectbox("Column for Pie Chart", columns, key='pie')
        st.sidebar.markdown('</div>', unsafe_allow_html=True)

        if pie_column:
            st.write("### Pie Chart")
            pie_data = df[pie_column].value_counts()
            fig, ax = plt.subplots()
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("coolwarm", len(pie_data)))
            ax.axis('equal')
            st.pyplot(fig)

    elif visualization_type == "Line Chart":
        st.sidebar.markdown('<div class="line-section">', unsafe_allow_html=True)
        line_x_axis = st.sidebar.selectbox("X-Axis for Line Chart", columns, index=0, key='line_x')
        line_y_axis = st.sidebar.selectbox("Y-Axis for Line Chart", columns, index=1, key='line_y')
        st.sidebar.markdown('</div>', unsafe_allow_html=True)

        if line_x_axis and line_y_axis:
            st.write("### Line Chart")
            fig, ax = plt.subplots()
            sns.lineplot(x=df[line_x_axis], y=df[line_y_axis], ax=ax)
            ax.set_xlabel(line_x_axis)
            ax.set_ylabel(line_y_axis)
            ax.set_title(f'Line chart of {line_x_axis} vs {line_y_axis}')
            st.pyplot(fig)

    elif visualization_type == "Bar Chart":
        st.sidebar.markdown('<div class="bar-section">', unsafe_allow_html=True)
        bar_column = st.sidebar.selectbox("Column for Bar Chart", columns, index=0, key='bar')
        st.sidebar.markdown('</div>', unsafe_allow_html=True)

        if bar_column:
            st.write("### Bar Chart")
            bar_data = df[bar_column].value_counts()
            fig, ax = plt.subplots()
            sns.barplot(x=bar_data.index, y=bar_data.values, ax=ax, palette="viridis")
            ax.set_xlabel(bar_column)
            ax.set_ylabel('Count')
            ax.set_title(f'Bar Chart of {bar_column}')
            st.pyplot(fig)

    elif visualization_type == "Histogram":
        st.sidebar.markdown('<div class="histogram-section">', unsafe_allow_html=True)
        hist_column = st.sidebar.selectbox("Column for Histogram", columns, index=0, key='histogram')
        st.sidebar.markdown('</div>', unsafe_allow_html=True)

        if hist_column:
            st.write("### Histogram")
            fig, ax = plt.subplots()
            sns.histplot(df[hist_column], bins=30, ax=ax, kde=True, color='skyblue')
            ax.set_xlabel(hist_column)
            ax.set_ylabel('Frequency')
            ax.set_title(f'Histogram of {hist_column}')
            st.pyplot(fig)

else:
    st.write("Please Upload a CSV or Excel file to Proceed")

# Adding a footer
st.markdown(
    """
    <style>
    footer {
        visibility: hidden;
    }
    footer:after {
        content:'Developed by Clinton Nkechi'; 
        visibility: visible;
        display: block;
        position: relative;
        padding: 5px;
        top: 2px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
