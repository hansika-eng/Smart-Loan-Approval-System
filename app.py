import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Smart Loan Approval System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

model = joblib.load("models/loan_approval_model.pkl")

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.stApp{
background:#0F172A;
color:white;
}

.block-container{
padding-top:2rem;
padding-left:3rem;
padding-right:3rem;
}

.hero{

padding:35px;

border-radius:20px;

background:linear-gradient(135deg,#2563EB,#1E40AF);

box-shadow:0px 10px 25px rgba(0,0,0,.4);

margin-bottom:25px;

}

.metric-card{

background:#1E293B;

padding:20px;

border-radius:15px;

text-align:center;

border:1px solid #334155;

transition:.3s;

}

.metric-card:hover{

transform:translateY(-5px);

}

.stButton>button{

background:#2563EB;

color:white;

height:55px;

border:none;

border-radius:10px;

font-size:18px;

font-weight:bold;

width:100%;

}

.stButton>button:hover{

background:#1D4ED8;

}

.footer{

text-align:center;

color:#94A3B8;

padding:20px;

}

</style>
""",unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/bank-building.png",
        width=90
    )

    st.title("Loan Dashboard")

    st.markdown("---")

    st.metric("🏆 Model","Gradient Boosting")

    st.metric("🎯 Accuracy","98.24%")

    st.metric("📊 Dataset","4269")

    st.metric("⚡ Version","2.0")

    st.markdown("---")

    st.subheader("Technologies")

    st.write("🐍 Python")

    st.write("📊 Streamlit")

    st.write("🤖 Scikit-Learn")

    st.write("📈 Plotly")

    st.write("🐼 Pandas")

    st.markdown("---")

    st.success("Developed by\n\n**Hansika Indukuri**")

# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown("""
<div style="
background:linear-gradient(90deg,#2563eb,#1e3a8a);
padding:30px;
border-radius:15px;
box-shadow:0 8px 25px rgba(0,0,0,.3);
margin-bottom:20px;
text-align:center;
">

<h1 style="
color:white;
margin-bottom:10px;
font-size:42px;
font-weight:700;
">
🏦 Smart Loan Approval System
</h1>

<p style="
color:#dbeafe;
font-size:18px;
margin:0;
">
AI Powered Credit Risk Assessment using Machine Learning
</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DASHBOARD STATS
# --------------------------------------------------

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric(
        "🎯 Accuracy",
        "98.24%",
        "Best Model"
    )

with c2:
    st.metric(
        "🏆 Model",
        "Gradient Boosting"
    )

with c3:
    st.metric(
        "📄 Dataset",
        "4269"
    )

with c4:
    st.metric(
        "⚡ Speed",
        "<1 sec"
    )

# ==========================================================
# LOAN APPLICATION FORM
# ==========================================================

st.markdown("## 📝 Loan Application")

st.write(
    "Fill in the applicant's details to predict the loan approval status."
)

st.markdown("---")

left, right = st.columns(2)

# ==========================================================
# LEFT COLUMN
# ==========================================================

with left:

    st.markdown("### 👤 Applicant Information")

    dependents = st.number_input(
        "👨‍👩‍👧 Number of Dependents",
        min_value=0,
        max_value=10,
        value=1,
        step=1
    )

    education = st.selectbox(
        "🎓 Education",
        [
            "Graduate",
            "Not Graduate"
        ]
    )

    self_employed = st.selectbox(
        "💼 Self Employed",
        [
            "No",
            "Yes"
        ]
    )

    income = st.number_input(
        "💰 Annual Income (₹)",
        min_value=0,
        value=500000,
        step=50000,
        help="Enter applicant's annual income."
    )

    loan_amount = st.number_input(
        "🏦 Loan Amount (₹)",
        min_value=0,
        value=1000000,
        step=50000
    )

# ==========================================================
# RIGHT COLUMN
# ==========================================================

with right:

    st.markdown("### 💳 Financial Details")

    loan_term = st.slider(
        "📅 Loan Term (Years)",
        min_value=1,
        max_value=30,
        value=12
    )

    cibil = st.slider(
        "📈 CIBIL Score",
        min_value=300,
        max_value=900,
        value=750
    )

    residential = st.number_input(
        "🏠 Residential Assets (₹)",
        min_value=0,
        value=500000,
        step=50000
    )

    commercial = st.number_input(
        "🏢 Commercial Assets (₹)",
        min_value=0,
        value=100000,
        step=50000
    )

    luxury = st.number_input(
        "💎 Luxury Assets (₹)",
        min_value=0,
        value=500000,
        step=50000
    )

    bank = st.number_input(
        "🏛 Bank Assets (₹)",
        min_value=0,
        value=300000,
        step=50000
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# QUICK SUMMARY
# ==========================================================

with st.expander("📋 Applicant Summary", expanded=False):

    c1, c2, c3 = st.columns(3)

    with c1:

        st.write("### Personal")

        st.write(f"Dependents : {dependents}")

        st.write(f"Education : {education}")

        st.write(f"Employment : {self_employed}")

    with c2:

        st.write("### Loan")

        st.write(f"Income : ₹{income:,}")

        st.write(f"Loan : ₹{loan_amount:,}")

        st.write(f"Term : {loan_term} Years")

    with c3:

        st.write("### Financial")

        st.write(f"CIBIL : {cibil}")

        st.write(f"Residential : ₹{residential:,}")

        st.write(f"Commercial : ₹{commercial:,}")

        st.write(f"Luxury : ₹{luxury:,}")

        st.write(f"Bank : ₹{bank:,}")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# PREDICT BUTTON
# ==========================================================

predict = st.button(
    "🚀 Analyze Loan Application",
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)
# ==========================================================
# PREDICTION ENGINE
# ==========================================================

if predict:

    with st.spinner("🔍 Analyzing loan application..."):

        education_value = 1 if education == "Graduate" else 0
        self_emp_value = 1 if self_employed == "Yes" else 0

        features = np.array([[
            dependents,
            education_value,
            self_emp_value,
            income,
            loan_amount,
            loan_term,
            cibil,
            residential,
            commercial,
            luxury,
            bank
        ]])

        prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]

        reject_prob = probabilities[0] * 100
        approve_prob = probabilities[1] * 100

        confidence = max(probabilities) * 100

    st.markdown("---")

    st.header("📊 Prediction Dashboard")

    left, right = st.columns([1.2, 1])

    # ==========================================
    # RESULT CARD
    # ==========================================

    with left:

        if prediction == 1:

            st.success("## ✅ LOAN APPROVED")

            risk = "🟢 LOW"

            st.balloons()

        else:

            st.error("## ❌ LOAN REJECTED")

            risk = "🔴 HIGH"

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

        with c2:

            st.metric(
                "Risk Level",
                risk
            )

        st.write("### Confidence")

        st.progress(confidence / 100)

        st.markdown("<br>", unsafe_allow_html=True)

        st.info(f"""
### Decision Summary

**Prediction :**
{"Approved" if prediction == 1 else "Rejected"}

**Approval Probability :**
{approve_prob:.2f}%

**Rejection Probability :**
{reject_prob:.2f}%

""")

    # ==========================================
    # DONUT CHART
    # ==========================================

    with right:

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=["Rejected", "Approved"],
                    values=[reject_prob, approve_prob],
                    hole=0.65,
                    textinfo="label+percent"
                )
            ]
        )

        fig.update_layout(
            title="Prediction Probability",
            template="plotly_dark",
            height=430,
            showlegend=True
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    # ==========================================
    # APPLICATION SUMMARY
    # ==========================================

    st.subheader("📋 Loan Application Summary")

    s1, s2, s3 = st.columns(3)

    with s1:

        st.info(f"""
### 👤 Applicant

Dependents : **{dependents}**

Education : **{education}**

Self Employed : **{self_employed}**
""")

    with s2:

        st.info(f"""
### 💰 Loan

Income : **₹ {income:,}**

Loan : **₹ {loan_amount:,}**

Term : **{loan_term} Years**
""")

    with s3:

        st.info(f"""
### 💳 Financial

CIBIL : **{cibil}**

Residential : **₹ {residential:,}**

Commercial : **₹ {commercial:,}**

Luxury : **₹ {luxury:,}**

Bank : **₹ {bank:,}**
""")

    # ==========================================
    # STORE HISTORY
    # ==========================================

    st.session_state.history.append({

        "Time": datetime.now().strftime("%H:%M:%S"),

        "Prediction":
        "Approved" if prediction == 1 else "Rejected",

        "Confidence":
        round(confidence, 2)

    })

    # ==========================================
    # HISTORY
    # ==========================================

    st.markdown("---")

    st.subheader("📜 Prediction History")

    history = pd.DataFrame(st.session_state.history)

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True
    )
    # ==========================================================
# EXTRA FEATURES
# ==========================================================

if predict:

    st.markdown("---")

    # ======================================================
    # AI RECOMMENDATIONS
    # ======================================================

    st.subheader("🧠 AI Financial Insights")

    recommendations = []

    if cibil < 650:
        recommendations.append(
            ("warning",
             "Improve your CIBIL score above 700 to significantly increase approval chances.")
        )

    if income < loan_amount:
        recommendations.append(
            ("warning",
             "Your requested loan amount is high compared to your annual income.")
        )

    if residential + commercial + luxury + bank < loan_amount:
        recommendations.append(
            ("warning",
             "Increasing your assets or collateral may improve loan eligibility.")
        )

    if prediction == 1:
        recommendations.append(
            ("success",
             "Your financial profile appears healthy based on the provided information.")
        )

    if len(recommendations) == 0:
        recommendations.append(
            ("info",
             "No major financial concerns were detected.")
        )

    for level, message in recommendations:

        if level == "success":
            st.success(message)

        elif level == "warning":
            st.warning(message)

        else:
            st.info(message)

    # ======================================================
    # FEATURE IMPORTANCE
    # ======================================================

    st.markdown("---")

    st.subheader("📊 Feature Importance")

    importance = pd.DataFrame({

        "Feature":[
            "Dependents",
            "Education",
            "Employment",
            "Income",
            "Loan Amount",
            "Loan Term",
            "CIBIL",
            "Residential Assets",
            "Commercial Assets",
            "Luxury Assets",
            "Bank Assets"
        ],

        "Importance":model.feature_importances_

    })

    importance = importance.sort_values(
        "Importance",
        ascending=False
    )

    st.bar_chart(
        importance.set_index("Feature")
    )

    # ======================================================
    # DOWNLOAD REPORT
    # ======================================================

    st.markdown("---")

    st.subheader("📥 Export Report")

    report = pd.DataFrame({

        "Field":[
            "Prediction",
            "Confidence",
            "Risk",
            "Income",
            "Loan Amount",
            "Loan Term",
            "CIBIL"
        ],

        "Value":[
            "Approved" if prediction==1 else "Rejected",
            f"{confidence:.2f}%",
            risk,
            income,
            loan_amount,
            loan_term,
            cibil
        ]

    })

    csv = report.to_csv(index=False).encode()

    st.download_button(

        "⬇ Download Prediction Report",

        csv,

        file_name="Loan_Prediction_Report.csv",

        mime="text/csv",

        use_container_width=True

    )

# ==========================================================
# MODEL INFORMATION
# ==========================================================

st.markdown("---")

with st.expander("📘 About This Model"):

    st.markdown("""

### Smart Loan Approval System

**Algorithm**
- Gradient Boosting Classifier

**Dataset**
- Loan Approval Dataset
- 4269 Applications

**Features**
- Dependents
- Education
- Employment
- Income
- Loan Amount
- Loan Term
- CIBIL Score
- Assets

**Target**
- Loan Approved / Rejected

**Accuracy**
- 98.24%

""")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown("""

<div style="text-align:center;padding:20px">

<h3>🏦 Smart Loan Approval System</h3>
<b>Python • Streamlit • Scikit-Learn • Plotly</b>

© 2026 Hansika Indukuri
AI & Data Science | KL University

</div>

""",unsafe_allow_html=True)