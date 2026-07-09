<h1 align="center">
🏦 Smart Loan Approval & Credit Risk Assessment System
</h1>

<p align="center">

Machine Learning powered Loan Approval Prediction Dashboard

</p>

<p align="center">

Python • Streamlit • Scikit-Learn • Plotly
<p align="center">

<img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
<img src="https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit">
<img src="https://img.shields.io/badge/Scikit--Learn-Gradient%20Boosting-orange?logo=scikitlearn">
<img src="https://img.shields.io/badge/Accuracy-98.24%25-brightgreen">
<img src="https://img.shields.io/badge/License-MIT-success">

</p>

</p>
**AI-Powered Loan Approval Prediction using Machine Learning**

Predict whether a loan application is likely to be **Approved** or **Rejected** using a trained **Gradient Boosting Machine Learning Model** with an interactive **Streamlit Dashboard**.

</p>

---

# 📖 Overview

Banks evaluate numerous financial and personal factors before approving a loan.

This project simulates that process using a Machine Learning model trained on historical loan application data. The application predicts whether a loan is likely to be approved while providing confidence scores, financial insights, interactive visualizations, and feature importance.

The application is built using **Python, Scikit-Learn, Streamlit, and Plotly** with a modern dashboard interface.

---

# ✨ Features

- 🤖 Machine Learning based Loan Prediction
- 📈 98.24% Prediction Accuracy
- ⚡ Instant Real-Time Prediction
- 📊 Interactive Dashboard
- 📉 Feature Importance Visualization
- 📋 Loan Application Summary
- 🧠 AI Financial Insights
- 📄 Export Prediction Report
- 🌙 Modern Dark Theme UI
- 📱 Responsive Streamlit Interface

---

# 🖼 Application Preview

## Dashboard & Loan Application

<img src="https://github.com/user-attachments/assets/f59a9276-8f61-4850-8159-c42230b1a2bb" width="100%">

## Loan Approved Prediction
<img width="1280" height="598" alt="image" src="https://github.com/user-attachments/assets/05296e44-b06c-4026-a91c-df63e8b83e7a" />

<img src="https://github.com/user-attachments/assets/1868fcc5-6305-48bf-bee3-252471ed5ea1" width="100%">

---

## Loan Rejected Prediction

<img src="https://github.com/user-attachments/assets/a8006c76-543f-44a9-9b89-a753d407aac6" width="100%">


##  AI Financial Insights & Feature Importance
<img src="https://github.com/user-attachments/assets/bbe19a32-cef3-40b8-9778-d8cc01df58ea" width="100%">

---

# 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- Gradient Boosting Classifier
- Pandas
- NumPy

### Visualization

- Plotly

### Frontend

- Streamlit

### Model Storage

- Pickle (.pkl)

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
Smart-Loan-Approval-System
│
├── app.py
├── README.md
├── requirements.txt
│
├── data
│   └── loan_approval_dataset.csv
│
├── models
│   └── loan_approval_model.pkl
│
├── notebooks
│   └── Loan_Approval.ipynb
│
└── .gitignore
```

---

# 🧠 Machine Learning Pipeline

The project follows the complete Machine Learning workflow.

### 1️⃣ Data Collection

Historical Loan Approval Dataset containing applicant and financial details.

### 2️⃣ Data Preprocessing

- Missing Value Handling
- Label Encoding
- Feature Selection

### 3️⃣ Model Training

Multiple machine learning algorithms were evaluated.

The **Gradient Boosting Classifier** achieved the highest accuracy.

### 4️⃣ Model Evaluation

Metrics used include:

- Accuracy
- Confusion Matrix
- Feature Importance

### 5️⃣ Model Deployment

The trained model is serialized using Pickle and deployed with Streamlit.

---

# 📊 Model Performance

| Metric | Value |
|---------|-------|
| Best Model | Gradient Boosting |
| Accuracy | **98.24%** |
| Dataset Size | **4269 Applications** |
| Prediction Time | Less than 1 Second |

---

# 📈 Input Features

The model considers the following applicant information.

| Feature |
|----------|
| Number of Dependents |
| Education |
| Self Employed |
| Annual Income |
| Loan Amount |
| Loan Term |
| CIBIL Score |
| Residential Assets |
| Commercial Assets |
| Luxury Assets |
| Bank Assets |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/hansika-eng/Smart-Loan-Approval-System.git
```

Move inside the project

```bash
cd Smart-Loan-Approval-System
```

Create a virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🌐 Live Demo

**Streamlit App**

https://smartloanai.streamlit.app
<img width="1280" height="581" alt="image" src="https://github.com/user-attachments/assets/f59a9276-8f61-4850-8159-c42230b1a2bb" />
<img width="1280" height="598" alt="image" src="https://github.com/user-attachments/assets/bca893cf-22b7-4a8c-b40e-470e6f5b8b77" />
<img width="1280" height="579" alt="image" src="https://github.com/user-attachments/assets/1868fcc5-6305-48bf-bee3-252471ed5ea1" />
<img width="1280" height="580" alt="image" src="https://github.com/user-attachments/assets/a8006c76-543f-44a9-9b89-a753d407aac6" />
<img width="1280" height="579" alt="image" src="https://github.com/user-attachments/assets/8c0e0d79-3e4a-444f-9bb1-fc934bb994d2" />
<img width="1280" height="572" alt="image" src="https://github.com/user-attachments/assets/bbe19a32-cef3-40b8-9778-d8cc01df58ea" />


# 💡 Future Improvements

- 🔐 User Authentication
- 📑 PDF Report Generation
- 💳 EMI Calculator
- ☁ Cloud Database Integration
- 📊 Multiple ML Model Comparison
- 🤖 SHAP Explainability
- 📈 Analytics Dashboard
- 📱 Mobile Optimized UI

---

# 🎯 Learning Outcomes

Through this project I gained practical experience in:

- Data Preprocessing
- Machine Learning Model Selection
- Feature Engineering
- Model Serialization
- Interactive Dashboard Development
- Streamlit Deployment
- Git & GitHub Version Control
- Data Visualization using Plotly

---

# 👩‍💻 Author

## Hansika Indukuri

**B.Tech Artificial Intelligence & Data Science**

KL University Hyderabad

### Connect with me

- GitHub: https://github.com/hansika-eng
- LinkedIn: *(Add your LinkedIn profile here)*

---

# ⭐ If you like this project

Please consider giving this repository a ⭐ on GitHub.

It motivates me to build more Machine Learning projects.

---

# 📜 License

This project is developed for educational and portfolio purposes.
