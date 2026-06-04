import streamlit as st
from model import chain

st.set_page_config(
    page_title="Email Intent & Urgency Detector",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Email Intent & Urgency Detector")

st.markdown(
    "Automatically classify incoming emails to help support teams prioritize and respond faster."
)

st.caption(
    "✅ Intent Classification • ⚡ Urgency Detection • 💬 Tone Analysis"
)

st.write("Enter an email to analyze its intent, urgency, and tone.")

email = st.text_area(
    "Enter Email Content",
    height=50,
    placeholder="Type or paste an email here..."
)

if st.button("Analyze Email", use_container_width=True):

    if not email.strip():
        st.warning("Please enter an email.")
    else:
        with st.spinner("Analyzing email..."):

            result = chain.invoke(
                {"problem": email}
            )

        st.success("Email analyzed successfully")

        st.subheader("Analysis Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                label="🎯 Intent",
                value=result.intent
            )

        with col2:
            st.metric(
                label="⚡ Urgency",
                value=result.urgency
            )

        with col3:
            st.metric(
                label="💬 Tone",
                value=result.tone
            )