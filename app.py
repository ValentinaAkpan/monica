import streamlit as st
import plotly.express as px
import pandas as pd

# Base value for Digital Economy GDP in 2010 (in billions of dollars)
base_gdp_2010 = 1500  # Example base value

# Annual growth rate (assumed average growth rate)
growth_rate = 0.1  # Example: 10% annual growth

# Generate GDP values for each year dynamically based on the growth rate
years_digital_economy = list(range(2010, 2022))  # 2010 to 2021
digital_economy_gdp = [base_gdp_2010 * (1 + growth_rate) ** (year - 2010) for year in years_digital_economy]

# Create DataFrames for Plotly
df_activities = pd.DataFrame({
    "Category": ["Infrastructure", "E-commerce", "Priced Digital Services", "Federal Nondefense Digital Services"],
    "Gross Output (in millions)": [1167116, 941970, 1592217, 420]
})

df_digital_economy_growth = pd.DataFrame({
    "Year": years_digital_economy,
    "GDP (in billions)": digital_economy_gdp
})

# Streamlit Dashboard Title
st.title("Digital Economy Visualization Dashboard")

# First Visualization: Digital Economy Breakdown by Major Activity
st.subheader("Digital Economy Breakdown by Major Activity (2021)")
fig1 = px.bar(df_activities, x="Gross Output (in millions)", y="Category", orientation='h',
              title="Gross Output by Major Activity", color="Category", height=400)
st.plotly_chart(fig1)

# Second Visualization: Digital Economy Growth Over Time (Calculated)
st.subheader("Digital Economy Growth Over Time (2010-2021)")
fig2 = px.line(df_digital_economy_growth, x="Year", y="GDP (in billions)",
               title="Digital Economy GDP Growth (Calculated)", markers=True)
st.plotly_chart(fig2)

# Summary of Findings
st.write("""
### Findings:
1. The **Digital Economy** has grown from **$1.5 trillion in 2010** to approximately **$3.7 trillion in 2021**, calculated based on an assumed **10% annual growth rate**.
2. The largest contributor in 2021 was **Priced Digital Services**, contributing over **$1.59 trillion**.
""")


import streamlit as st
import plotly.express as px
import pandas as pd

# Data for Number and Percent Distribution of Establishments in Green Goods and Services by Industry Sector (2009)
data = {
    "Industry Sector": [
        "Construction", 
        "Professional and Business Services", 
        "Other Services (Repair and Maintenance)", 
        "Natural Resources and Mining", 
        "Information", 
        "Manufacturing", 
        "Trade, Transportation, and Utilities", 
        "Public Administration", 
        "Education and Health Services", 
        "All Other Sectors"
    ],
    "Number of Establishments": [
        820700, 779100, 183300, 88700, 77000, 77700, 49300, 42100, 26400, 10400
    ],
    "Percent Distribution": [
        38.1, 36.2, 8.5, 4.1, 3.6, 3.6, 2.3, 2.0, 1.2, 0.5
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Visualization 1: Bar chart for number of establishments by industry
fig1 = px.bar(df, x="Industry Sector", y="Number of Establishments", title="Number of Establishments Producing Green Goods and Services (2009)",
              labels={"Number of Establishments": "Number of Establishments"},
              height=400)
st.plotly_chart(fig1)

# Visualization 2: Percent distribution by industry
fig2 = px.pie(df, values='Percent Distribution', names='Industry Sector', title="Percent Distribution of Green Goods and Services by Industry (2009)")
st.plotly_chart(fig2)

# Summary of Findings
st.write("""
### Findings from the BLS Green Jobs Initiative:
1. The **Construction** and **Professional and Business Services** sectors dominate in terms of establishments producing green goods and services, comprising nearly 75% of the total.
2. The **BLS green jobs initiative** used two measurement approaches:
   - The **output approach** focuses on establishments producing green goods and services.
   - The **process approach** tracks establishments that use environmentally friendly practices, regardless of the products they create.
3. Tracking was halted in 2013, leaving a gap in national data on green jobs.
""")

import streamlit as st
import plotly.express as px
import pandas as pd

# Simulated Green Jobs Data (2010-2013) from BLS before tracking halted
years_bls_tracking = [2010, 2011, 2012, 2013]
green_job_values_bls = [1500, 1600, 1700, 1750]  # Example in thousands

# Simulated gap post-2013 (no national tracking)
years_no_tracking = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
green_job_values_gap = [None] * len(years_no_tracking)  # No data due to halted tracking

# Combine years and values into one DataFrame
df_green_jobs = pd.DataFrame({
    "Year": years_bls_tracking + years_no_tracking,
    "Green Jobs (in thousands)": green_job_values_bls + green_job_values_gap
})

# Create line chart
fig = px.line(df_green_jobs, x="Year", y="Green Jobs (in thousands)", 
              title="Tracking of Green Jobs Halted After 2013",
              markers=True)

# Highlight the gap where tracking stopped
fig.update_traces(connectgaps=False)  # This creates a gap after 2013
fig.add_annotation(text="Tracking Halted in 2013", x=2013, y=1750, showarrow=True, arrowhead=2)

# Display the chart in Streamlit
st.plotly_chart(fig)

# Explanation
st.write("""
### Key Points:
- **Tracking of green jobs was consistent** from 2010 to 2013, as part of the **BLS Green Jobs Initiative**.
- **Tracking was halted in 2013** due to budget cuts, leading to a gap in national green job data.
- Since 2013, no comprehensive national-level green jobs data has been collected by the **BLS**, leaving a gap in understanding the growth of the green economy.
""")
import streamlit as st
import plotly.express as px
import pandas as pd

# Simulated Green Jobs Data (2010-2013) from BLS before tracking halted
years_bls_tracking = [2010, 2011, 2012, 2013]
green_job_values_bls = [1500, 1600, 1700, 1750]  # Example in thousands

# Simulated gap post-2013 (no national tracking)
years_no_tracking = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
green_job_values_gap = [None] * len(years_no_tracking)  # No data due to halted tracking

# Combine years and values into one DataFrame
df_green_jobs = pd.DataFrame({
    "Year": years_bls_tracking + years_no_tracking,
    "Green Jobs (in thousands)": green_job_values_bls + green_job_values_gap
})

# Base value for Digital Economy GDP in 2010 (in billions of dollars)
base_gdp_2010 = 1500  # Example base value
growth_rate = 0.1  # 10% annual growth

# Generate GDP values for each year dynamically based on the growth rate
years_digital_economy = list(range(2010, 2022))  # 2010 to 2021
digital_economy_gdp = [base_gdp_2010 * (1 + growth_rate) ** (year - 2010) for year in years_digital_economy]

# Create DataFrame for Digital Economy GDP
df_digital_economy = pd.DataFrame({
    "Year": years_digital_economy,
    "GDP (in billions)": digital_economy_gdp
})

# Create Green Jobs chart
fig_green_jobs = px.line(df_green_jobs, x="Year", y="Green Jobs (in thousands)",
                         title="Green Jobs Tracking Halted After 2013", markers=True)
fig_green_jobs.update_traces(connectgaps=False)  # Creates a gap in the data
fig_green_jobs.add_annotation(text="Tracking Halted in 2013", x=2013, y=1750, showarrow=True, arrowhead=2)

# Create Digital Economy chart
fig_digital_economy = px.line(df_digital_economy, x="Year", y="GDP (in billions)",
                              title="Digital Economy Growth Over Time (2010-2021)", markers=True)

# Create a layout for side-by-side comparison
st.title("Comparison of Green Jobs and Digital Economy Growth")

# Explanation of sequestration and halted green jobs tracking
st.write("""
### Sequestration and Halted Green Jobs Tracking
On March 1, 2013, President Obama ordered into effect the across-the-board spending cuts (commonly referred to as sequestration) required by the Balanced Budget and Emergency Deficit Control Act, as amended. Under the order, the Bureau of Labor Statistics (BLS) was required to cut its current budget by more than $30 million, about 5 percent of the 2013 appropriation, by September 30, 2013. 

In order to achieve these savings and protect core programs, the BLS eliminated two programs, including all **'measuring green jobs'** products. These products included data on employment by industry and occupation for businesses that produce green goods and services, data on the occupations and wages of jobs related to green technologies and practices, and green career information publications. [More info on the sequestration](https://www.bls.gov/bls/sequester_info.htm).
""")

# Explain the context of the comparison
st.write("""
### Key Insight:
- While **U.S. green jobs tracking** was halted after 2013, the **digital economy** has been consistently tracked and shows steady growth.
- This comparison highlights the disparity in tracking two sectors that are vital to understanding economic growth in the U.S.
""")

# Display the two charts side by side
col1, col2 = st.columns(2)

with col1:
    st.subheader("Green Jobs (2010-2013)")
    st.plotly_chart(fig_green_jobs)

with col2:
    st.subheader("Digital Economy (2010-2021)")
    st.plotly_chart(fig_digital_economy)

