import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="Data Analyst Assessment", layout="wide")

st.title("📊 Data Analyst Training Assessment")
st.markdown("---")

# Form
with st.form("assessment_form"):
    name = st.text_input("Your Name:", placeholder="Enter your name")
    email = st.text_input("Email:", placeholder="your.email@example.com")
    
    # SQL Section
    st.subheader("SQL Knowledge")
    sql_score = st.slider("SQL Proficiency (1-5):", 1, 5, 3)
    sql_experience = st.selectbox("SQL Experience:", ["Beginner", "Intermediate", "Advanced"])
    
    # Python Section
    st.subheader("Python Knowledge")
    python_score = st.slider("Python Proficiency (1-5):", 1, 5, 3)
    python_experience = st.selectbox("Python Experience:", ["Beginner", "Intermediate", "Advanced"])
    
    # Power BI Section
    st.subheader("Power BI Knowledge")
    powerbi_score = st.slider("Power BI Proficiency (1-5):", 1, 5, 3)
    powerbi_experience = st.selectbox("Power BI Experience:", ["Beginner", "Intermediate", "Advanced"])
    
    # Comments
    comments = st.text_area("Additional Comments:", placeholder="Share your thoughts...")
    
    # Submit
    submitted = st.form_submit_button("📤 Submit Assessment")

if submitted:
    if not name or not email:
        st.error("❌ Please fill in Name and Email!")
    else:
        # Save to JSON file
        response = {
            "timestamp": datetime.now().isoformat(),
            "name": name,
            "email": email,
            "sql_score": sql_score,
            "sql_experience": sql_experience,
            "python_score": python_score,
            "python_experience": python_experience,
            "powerbi_score": powerbi_score,
            "powerbi_experience": powerbi_experience,
            "comments": comments
        }
        
        # Save to file
        try:
            with open("responses.json", "a") as f:
                json.dump(response, f)
                f.write("\n")
            
            st.success("✅ Assessment submitted successfully!")
            st.balloons()
            
            # Show results
            st.subheader("Your Assessment Results:")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("SQL Score", f"{sql_score}/5")
            with col2:
                st.metric("Python Score", f"{python_score}/5")
            with col3:
                st.metric("Power BI Score", f"{powerbi_score}/5")
                
        except Exception as e:
            st.error(f"❌ Error saving response: {e}")
