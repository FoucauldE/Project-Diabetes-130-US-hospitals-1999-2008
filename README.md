# Project-Diabetes-130-US-hospitals-1999-2008

## Description

This project addresses the critical issue of early hospital readmissions among diabetes patients, a growing global health concern. With 463 million adults affected by diabetes as of 2019 and an expected rise to 700 million by 2045, effective management of diabetes is crucial. Our study spans 10 years of data (1999-2008) from 130 US hospitals, focusing on diabetic patients who underwent various treatments and had hospital stays of up to 14 days. The aim is to identify the primary factors leading to early readmission.

To address this, we employed a Random Forest algorithm with a class balancing parameter, which proved most efficient in our case. A key strength of our solution is its ability to explain the likelihood of readmission using SHAP (SHapley Additive exPlanations), a Python library that reveals the positive or negative impact of each feature on our prediction. This approach not only ensures accuracy but also provides transparency and ease of use. 

The solution is already accessible and testable via our website : https://project-diabetes-130-us-hospitals-1999-2008-f2azfjbcodx3anldgj.streamlit.app/

## Installation

This project requires Python 3.10.12. Ensure you have the correct version of Python installed on your system.

## Environnement Setup

It is recommended to use a virtual environment to avoid dependency conflicts with other projects. To create and activate a virtual environment:

On Unix or MacOS:
python3 -m venv my_env
source my_env/bin/activate

On Windows:
python -m venv my_env
my_env\Scripts\activate

## Installing Dependencies

Install all necessary dependencies by running:
pip install -r requirements.txt

## Usage

To try our solution, you can directly visit our website : https://project-diabetes-130-us-hospitals-1999-2008-f2azfjbcodx3anldgj.streamlit.app/

To launch our WebApp locally, navigate to the project directory and run the following command:
streamlit run .\app\Home.py

## Features

🆕 Evaluate the readmission risk for a new patient based on clinical data

📈 View statistical insights from our training dataset to understand broader trends

📑 See more details about how we built this model

👥 Meet and discover the team that worked on this project
