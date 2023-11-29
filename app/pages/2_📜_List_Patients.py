import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="List Patients", page_icon="🏥", layout="wide")

st.markdown("# Patients List")
st.sidebar.header("List Patients")


# Function to load and preprocess data
def load_data():
    df = pd.read_csv('app/asset/diabetic_data.csv')
    # Convert readmission status to a categorical variable with color coding
    df['readmit_color'] = np.where(df['readmitted'] == '<30', 'red', 'green')
    return df


# Function to display the table with color coding
def color_row(row):
    # Define colors with transparency using rgba
    red_color = 'rgba(217,83,79, 0.5)'  # 50% transparency
    green_color = 'rgba(92,184,92, 0.5)'  # 50% transparency

    if row['readmit_color'] == 'red':
        return [f'background-color: {red_color}'] * len(row)
    else:
        return [f'background-color: {green_color}'] * len(row)


def display_table(df):
    # Pagination settings
    rows_per_page = 25
    n_pages = len(df) // rows_per_page + (1 if len(df) % rows_per_page else 0)
    page_number = st.number_input('Page Number', min_value=1, max_value=n_pages, value=1)
    start_row = (page_number - 1) * rows_per_page
    end_row = start_row + rows_per_page

    # Display the subset of the dataframe
    subset_df = df.iloc[start_row:end_row]

    # Apply the styling
    st.dataframe(subset_df.style.apply(color_row, axis=1))


# Function to display figures for variable distribution
def display_figures(data):
    st.write("### Distribution Figures")

    # Set the Seaborn style
    sns.set_style("darkgrid")
    palette = {"<30": '#d9534f', '>=30': '#5cb85c'}

    # Afficher les figures dans des colonnes
    col1, col2 = st.columns(2)

    with col1:
        # Age distribution
        data['readmitted_category'] = data['readmitted'].apply(lambda x: '<30' if x == '<30' else '>=30')

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data, x='age', hue='readmitted_category', multiple="dodge", ax=ax, palette=palette)
        plt.tight_layout()
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of Age by Readmission Status</h3>",
                    unsafe_allow_html=True)
        st.pyplot(fig)

    with col2:
        # Gender distribution
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of gender</h3>",
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(data, x='gender', hue='readmitted_category', ax=ax, palette=palette)
        plt.tight_layout()
        st.pyplot(fig)

    with col1:
        # Race distribution
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of 'Race'</h3>",
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(data, y='race', hue='readmitted_category', ax=ax, palette=palette)
        plt.tight_layout()
        ax.tick_params(axis='x', rotation=0)
        st.pyplot(fig)

    with col2:
        admission_source_descriptions = {
            1: "Physician Referral",
            2: "Clinic Referral",
            3: "HMO Referral",
            4: "Transfer from a hospital",
            5: "Transfer from a Skilled Nursing Facility (SNF)",
            6: "Transfer from another health care facility",
            7: "Emergency Room",
            8: "Court/Law Enforcement",
            10: "Transfer from critial access hospital",
            11: "Normal Delivery",
            12: "Premature Delivery",
            13: "Sick Baby",
            14: "Extramural Birth",
            15: "Not Available",
            17: "NULL",
            18: "Transfer From Another Home Health Agency",
            19: "Readmission to Same Home Health Agency",
            20: "Not Mapped",
            21: "Unknown/Invalid",
            22: "Transfer from hospital inpt/same fac reslt in a sep claim",
            23: "Born inside this hospital",
            24: "Born outside this hospital",
            25: "Transfer from Ambulatory Surgery Center",
            26: "Transfer from Hospice"
        }
        data['admission_source_description'] = data['admission_source_id'].map(admission_source_descriptions)
        # Admission source id distribution
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of Admission Source</h3>",
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(data, y='admission_source_description', hue='readmitted_category', ax=ax, palette=palette)
        plt.tight_layout()
        ax.tick_params(axis='x', rotation=0)
        st.pyplot(fig)

def display_figures_2(data):

    # Setting the aesthetic style of the plots
    sns.set(style="darkgrid")
    col1, col2 = st.columns(2)

    with col1:
        # Time in hospital
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of Time in Hospital</h3>",
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data['time_in_hospital'], kde=True, ax=ax, color='green')
        plt.tight_layout()
        st.pyplot(fig)
        st.markdown(
            "<br><br>", unsafe_allow_html=True)

    with col2:
        # Num medication distribution
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of Num Medications</h3>",
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data['num_medications'], ax=ax)
        plt.tight_layout()
        st.pyplot(fig)
        st.markdown(
            "<p style='text-align: center; color: lightblue;'>As a reminder, num_medication is the number of distinct "
            "generic drugs administered during the encounter.</p>", unsafe_allow_html=True)

    with col1:
        # Readmission distribution
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of Readmission Status</h3>",
                    unsafe_allow_html=True)

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(data['readmitted'], ax=ax, palette='muted')
        plt.tight_layout()
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

    with col2:
        # Distrubution of admission type
        admission_type_descriptions = {
            1: "Emergency",
            2: "Urgent",
            3: "Elective",
            4: "",
            5: "Not Available",
            6: "NULL",
            7: "Trauma Center",
            8: ""
        }

        # Calculer la distribution des types d'admission
        admission_counts = data['admission_type_id'].map(admission_type_descriptions).value_counts()

        # Créer un pie plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.pie(admission_counts, labels=admission_counts.index, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')  # Assure que le pie est dessiné comme un cercle

        # Affichage du titre
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of Admission Type</h3>",
                    unsafe_allow_html=True)

        st.pyplot(fig)

    with col1:
        # Missing data visualization
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of Missing Values</h3>",
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 6))
        missing = data.replace('?', pd.NA).isna().mean().sort_values(ascending=False)
        missing = missing[missing > 0]
        sns.barplot(x=missing, y=missing.index, ax=ax, palette='winter')
        plt.tight_layout()
        st.pyplot(fig)



def correlation_heatmap(data):
    # Correlation analysis among numerical features and with the target variable
    numerical_features = data.select_dtypes(include=['int64', 'float64'])
    correlation_matrix = numerical_features.corr(method='spearman')

    # Plotting the correlation matrix
    st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Spearman Correlation Matrix for Numeric Values</h3>",
                unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='Blues')
    st.pyplot(fig)


df = load_data()
display_table(df)

# Menu déroulant pour la sélection du graphique
option = st.selectbox(
    "Choisissez les graphiques à afficher:",
    ('Sélectionnez', 'Patient characteristics', 'Medical Statistics', 'Correlations')
)

# Afficher le graphique en fonction de la sélection
if option == 'Patient characteristics':
    display_figures(df)
elif option == 'Medical Statistics':
    display_figures_2(df)
elif option == 'Correlations':
    correlation_heatmap(df)
else:
    st.write("Sélectionnez un graphique à afficher.")

