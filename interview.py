import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the cleaned CSV file
df = pd.read_csv('interview_foundations_cleaned.csv')

# Streamlit page title
st.title('Interview Foundations Data Analysis')

# Introduce the data and its purpose
st.markdown("""
### About this Data
This dataset contains responses from various organizations about the efficiency and transparency of their funding processes. 
You can select a question from the sidebar.
""")

# Create a sidebar for selecting the question (filter)
st.sidebar.title('Choose a Question to Visualize')
option = st.sidebar.selectbox('Select a question to visualize:', ('Q2', 'Q3', 'Q4', 'Q5'))

# Cleaning up any inconsistent 'No' values by stripping spaces
def clean_responses(column_name):
    df[column_name] = df[column_name].str.strip()

# Clean each relevant column
clean_responses('Q2 - Do you believe that the current funding processes of corporate and philanthropic giving officers are efficient?')
clean_responses('Q3 - Do you think the current process for distributing funding earmarked for social justice topics is transparent and reliable?')
clean_responses('Q4 - Do you believe that the current funding and reporting processes of corporate and philanthropic giving reflect the experiences of the communities they hope to reach?')
clean_responses('Q5 - Would you be interested in establishing more transparent relationships with community groups and finance organizations?')

# Function to plot bar chart using Plotly
def plot_bar_chart(data, title, xlabel, ylabel):
    fig = px.bar(data, barmode='stack', title=title)
    fig.update_layout(
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        legend_title="Responses",
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.05
        )
    )
    # Adding hover template to show only the number without "Count"
    fig.update_traces(hovertemplate='%{y}')
    st.plotly_chart(fig)

# Donut Chart Function
def create_donut_chart(data, question_title):
    values = data.value_counts().values
    labels = data.value_counts().index

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5, textinfo='label+percent', insidetextorientation='auto')])
    fig.update_traces(hoverinfo='label+value', textfont_size=15, marker=dict(line=dict(color='white', width=2)))
    fig.update_layout(
        title=question_title,
        annotations=[dict(text='Organizations', x=0.5, y=0.5, font_size=20, showarrow=False)]
    )
    st.plotly_chart(fig)

# Get the data based on the selected question
if option == 'Q2':
    selected_data = df['Q2 - Do you believe that the current funding processes of corporate and philanthropic giving officers are efficient?']
    sector_data = df.groupby('Q1 -What is your industry sector?')['Q2 - Do you believe that the current funding processes of corporate and philanthropic giving officers are efficient?'].value_counts().unstack().fillna(0)
    question_title = "Q2: Do you believe that the current funding processes of corporate and philanthropic giving officers are efficient?"

elif option == 'Q3':
    selected_data = df['Q3 - Do you think the current process for distributing funding earmarked for social justice topics is transparent and reliable?']
    sector_data = df.groupby('Q1 -What is your industry sector?')['Q3 - Do you think the current process for distributing funding earmarked for social justice topics is transparent and reliable?'].value_counts().unstack().fillna(0)
    question_title = "Q3: Do you think the current process for distributing funding earmarked for social justice topics is transparent and reliable?"

elif option == 'Q4':
    selected_data = df['Q4 - Do you believe that the current funding and reporting processes of corporate and philanthropic giving reflect the experiences of the communities they hope to reach?']
    sector_data = df.groupby('Q1 -What is your industry sector?')['Q4 - Do you believe that the current funding and reporting processes of corporate and philanthropic giving reflect the experiences of the communities they hope to reach?'].value_counts().unstack().fillna(0)
    question_title = "Q4: Do you believe that the current funding and reporting processes of corporate and philanthropic giving reflect the experiences of the communities they hope to reach?"

elif option == 'Q5':
    selected_data = df['Q5 - Would you be interested in establishing more transparent relationships with community groups and finance organizations?']
    sector_data = df.groupby('Q1 -What is your industry sector?')['Q5 - Would you be interested in establishing more transparent relationships with community groups and finance organizations?'].value_counts().unstack().fillna(0)
    question_title = "Q5: Would you be interested in establishing more transparent relationships with community groups and finance organizations?"

# Display both charts for the selected question
st.markdown(f"## {question_title}")
plot_bar_chart(sector_data, question_title, 'Industry Sector', 'Count of Responses')

create_donut_chart(selected_data, question_title)
