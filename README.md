# 📊 Customer Retention & Churn Analysis

## 📌 Project Overview

This project analyzes customer churn using the Telco Customer Churn dataset. The objective is to identify the major factors influencing customer retention and provide actionable business recommendations to reduce customer churn.

---

## 🎯 Objectives

- Analyze overall customer churn
- Identify high-risk customer segments
- Explore customer lifetime patterns
- Recommend strategies to improve retention
- Build an interactive Streamlit dashboard

---

## 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

The dataset contains customer demographics, subscription details, payment methods, tenure, monthly charges, total charges, and churn status.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- Plotly
- Streamlit
- Jupyter Notebook

---

## 📁 Project Structure

```text
FUTURE_DS_02/
│
├── app.py
├── README.md
├── requirements.txt
├── data/
├── processed_data/
├── images/
├── notebooks/
└── .venv/
```

---

## 📊 Dashboard Preview

### Dashboard Overview

![Dashboard Overview](images/dashboard_overview.png)

### Customer Segmentation

![Customer Segmentation](images/customer_segmentation.png)

### Customer Lifetime Analysis

![Customer Lifetime](images/customer_lifetime.png)

### Business Insights

![Business Insights](images/business_insights.png)

---

## 🔍 Key Insights

- Overall customer churn rate is **26.58%**.
- Month-to-month contracts experience the highest churn.
- Fiber optic customers are significantly more likely to churn.
- Electronic Check users have the highest churn among payment methods.
- Most churn occurs during the early months of the customer lifecycle.
- Customers with higher monthly charges are more likely to leave.

---

## 💡 Business Recommendations

- Encourage long-term contracts through discounts and loyalty programs.
- Improve onboarding and engagement during the first year.
- Investigate Fiber optic customer dissatisfaction.
- Promote automatic payment methods.
- Offer personalized retention campaigns for high-risk customers.

---

## ▶️ Running the Dashboard

```bash
git clone <repository-url>

cd FUTURE_DS_02

source .venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

---

## 👨‍💻 Author

**Durlabh Thareja**

Future Interns – Data Science & Analytics Internship (Task 2)
