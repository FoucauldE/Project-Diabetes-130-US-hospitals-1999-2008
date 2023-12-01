import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Statistics", page_icon="🏥", layout="wide")

st.markdown("# Statistics")
#st.sidebar.header("List Patients")


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

    # Set the Seaborn style
    sns.set_style("darkgrid")
    palette = {"<30": '#d9534f', '>=30': '#5cb85c'}

    # Afficher les figures dans des colonnes
    col1, col2 = st.columns(2)
    data['readmitted_category'] = data['readmitted'].apply(lambda x: '<30' if x == '<30' else '>=30')

    with col1:
        # Age distribution        
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
    data['readmitted_category'] = data['readmitted'].apply(lambda x: '<30' if x == '<30' else '>=30')

    with col1:
        # Time in hospital
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of Time in Hospital</h3>",
                    unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data['time_in_hospital'], ax=ax, color='green', alpha=0.5)
        plt.tight_layout()
        st.pyplot(fig)

    with col2:
        # Num medication distribution
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of Lab Procedures</h3>",
                    unsafe_allow_html=True)
        fig = plt.figure(figsize = (10, 6))
        a = sns.kdeplot(data.loc[(data['readmitted_category'] == '>=30'), "num_lab_procedures"] ,
                        color = "g", fill = True, label = "Not Readmitted")
        a = sns.kdeplot(data.loc[(data['readmitted_category'] == '<30'), "num_lab_procedures"] ,
                        color = "r", fill = True, label = "Readmitted")
        a.legend()
        a.set_xlabel("Number of Lab Procedures")
        a.set_ylabel("Frequency")
        a.set_title("Distribution of Number Lab Procedures")
        plt.tight_layout()
        st.pyplot(fig)

    with col1:
        # Readmission distribution
        st.markdown(f"<h3 style='text-align: center; color: lightblue;'>Distribution of Readmission Status</h3>",
                    unsafe_allow_html=True)

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(data, x='readmitted', ax=ax, palette='muted')
        plt.tight_layout()        
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


def significance(data):
    results_significance = [('race', 0.23267994798808408),
        ('gender', 0.35884077972245254),
        ('discharge_disposition_id', 1.138739423681438e-204),
        ('admission_source_id', 1.0111160395779867e-08),
        ('metformin', 1.0936911695576979e-12),
        ('repaglinide', 0.007295458994734808),
        ('nateglinide', 0.7028757443394432),
        ('chlorpropamide', 0.4332785882619724),
        ('glimepiride', 0.07337966332272826),
        ('acetohexamide', 1.0),
        ('glipizide', 0.009281141787542569),
        ('glyburide', 0.2010981481705423),
        ('tolbutamide', 0.4798384209042891),
        ('pioglitazone', 0.0944357815861515),
        ('rosiglitazone', 0.14279012804105184),
        ('acarbose', 0.21899836701759287),
        ('miglitol', 0.16190490135183944),
        ('troglitazone', 1.0),
        ('tolazamide', 0.7654805302993656),
        ('examide', 1.0),
        ('citoglipton', 1.0),
        ('insulin', 4.137171762772658e-41),
        ('glyburide-metformin', 0.7555735918159463),
        ('glipizide-metformin', 1.0),
        ('glimepiride-pioglitazone', 1.0),
        ('metformin-rosiglitazone', 1.0),
        ('metformin-pioglitazone', 1.0),
        ('change', 5.166626196585065e-10),
        ('diabetesMed', 5.602389438425908e-18),
        ('diag_1_Cancers and Neoplasms', 0.04339576446786591),
        ('diag_1_Cardiovascular Diseases', 0.048431873701263166),
        ('diag_1_Diabetes', 1.5913353431438913e-08),
        ('diag_1_Digestive, Genitourinary, and Skin Disorders',
        0.0028738396624186768),
        ('diag_1_General Symptoms, Injuries, and Other Conditions',
        0.8624677973214012),
        ('diag_1_Infectious Diseases', 0.6425181885086366),
        ('diag_1_Mental and Neurological Disorders', 0.4791863238608238),
        ('diag_1_Musculoskeletal, Connective Tissue, and Congenital Disorders',
        0.0001237150943101158),
        ('diag_1_Other Chronic Diseases', 0.9677891060439296),
        ('diag_1_Uncategorized', 3.2614352069957074e-05),
        ('diag_2_Cancers and Neoplasms', 1.2770087037962548e-09),
        ('diag_2_Cardiovascular Diseases', 0.41509325449666457),
        ('diag_2_Diabetes', 0.027641776918696924),
        ('diag_2_Digestive, Genitourinary, and Skin Disorders',
        7.709321324528187e-06),
        ('diag_2_General Symptoms, Injuries, and Other Conditions',
        0.4910300230559891),
        ('diag_2_Infectious Diseases', 0.24314525573616685),
        ('diag_2_Mental and Neurological Disorders', 0.6258600234716997),
        ('diag_2_Musculoskeletal, Connective Tissue, and Congenital Disorders',
        0.0967133657811467),
        ('diag_2_Other Chronic Diseases', 0.01649553977191982),
        ('diag_2_Uncategorized', 6.7526967371645e-06),
        ('diag_3_Cancers and Neoplasms', 2.7460215258652996e-05),
        ('diag_3_Cardiovascular Diseases', 0.0031082551194845202),
        ('diag_3_Diabetes', 1.3184368105975647e-05),
        ('diag_3_Digestive, Genitourinary, and Skin Disorders',
        6.330790546678596e-15),
        ('diag_3_General Symptoms, Injuries, and Other Conditions',
        0.7230250564646096),
        ('diag_3_Infectious Diseases', 1.0),
        ('diag_3_Mental and Neurological Disorders', 0.3423040872250604),
        ('diag_3_Musculoskeletal, Connective Tissue, and Congenital Disorders',
        0.4342132181037388),
        ('diag_3_Other Chronic Diseases', 0.883651685663654),
        ('diag_3_Uncategorized', 3.196555085457828e-05),
        ('payer_code_Government Programs', 2.3084862813426165e-06),
        ('payer_code_Managed Care and Networks', 0.0020262614061112784),
        ('payer_code_Other', 0.00798565423349171),
        ('payer_code_Private Insurance', 4.2679380733088576e-08),
        ('payer_code_Self-Pay and Other Plans', 2.1600805812341517e-06),
        ('payer_code_Specialized Programs', 0.7618048003475828),
        ('medical_specialty_Diagnostic and Therapeutic Services',
        0.23605949922847264),
        ('medical_specialty_Emergency Medicine and Critical Care', 1.0),
        ('medical_specialty_General Practice and Internal Medicine',
        0.12828320233389462),
        ('medical_specialty_Other', 0.00018359895982504397),
        ('medical_specialty_Other Specialties and Miscellaneous',
        0.06834828321684588),
        ('medical_specialty_Pediatrics and Pediatric Subspecialties',
        4.6606593549004113e-07),
        ('medical_specialty_Specialized Organ and System Experts',
        0.0011264815056693683),
        ('medical_specialty_Surgery and Surgical Specialties', 0.037746082437865015),
        ("medical_specialty_Women's Health and Obstetrics/Gynecology",
        5.8384715853603405e-09),
        ('admission_type_id_Elective', 0.00022045204369396804),
        ('admission_type_id_Newborn', 1.0),
        ('admission_type_id_Other', 0.07580495024247479),
        ('admission_type_id_Urgent', 1.2240289899892896e-05),
        ('A1Cresult_>7', 0.027929083731195327),
        ('A1Cresult_>8', 0.00011686209774542518),
        ('A1Cresult_Norm', 0.0006038661764709982),
        ('max_glu_serum_>200', 0.11915367630137202),
        ('max_glu_serum_>300', 0.0003930977848677422),
        ('max_glu_serum_Norm', 0.768208172749456)]
    significant_df = pd.DataFrame(results_significance, columns=['Column', 'P-value'])
    
    significant_df = significant_df.sort_values(by='P-value')

    st.markdown(f"<h3 style='text-align: center; color: lightblue;'>P-value of Each Column with Target Variable</h3>",
                unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(14, 16))
    sns.barplot(x='P-value', y='Column', data=significant_df, orient='h', palette='winter')
    plt.axvline(x=0.05, color='red', linestyle='--')

    plt.xlabel('P-value')
    plt.ylabel('Columns')    

    plt.tight_layout()
    st.pyplot(fig)

def correlation_heatmap(data):
    data['readmitted_category'] = data['readmitted'].apply(lambda x: 1 if x == '<30' else 0)
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
    "Choose the graphics to display:",
    ('Select', 'Patient characteristics', 'Medical Statistics', 'Correlations')
)

# Afficher le graphique en fonction de la sélection
if option == 'Patient characteristics':
    display_figures(df)
elif option == 'Medical Statistics':
    display_figures_2(df)
elif option == 'Correlations':
    significance(df)
    correlation_heatmap(df)
else:
    st.write("Select a graphic")

