import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌟", layout="wide")

# Tailwind-Like Custom Styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            color: #1E40AF; /* Tailwind blue-900 */
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subheader {
            text-align: center;
            font-size: 18px;
            font-weight: 500;
            color: #64748B; /* Tailwind slate-500 */
            margin-bottom: 20px;
        }
        .card {
            background-color: #F1F5F9; /* Tailwind slate-100 */
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin: 10px 0;
        }
        .button {
            background-color: #22C55E; /* Tailwind green-500 */
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            font-weight: bold;
            text-align: center;
            display: inline-block;
            margin-top: 10px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #15803D; /* Tailwind green-700 */
        }
    </style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<div class="title">🌟 Growth Mindset Challenge</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Believe in Your Potential to Learn and Grow!</div>', unsafe_allow_html=True)

    # Display Card
    st.markdown('<div class="card">💡 A **Growth Mindset** helps you embrace challenges and learn from mistakes!</div>', unsafe_allow_html=True)

    st.header("🔥 Choose Your Challenge!")
    challenge = st.selectbox("Pick a challenge for today:",
                              ["Reflect on a recent mistake and what you learned",
                               "Encourage a friend to keep trying",
                               "Try a new skill outside your comfort zone",
                               "Replace negative thoughts with positive ones"])

    if st.button("🚀 Accept the Challenge!"):
        st.markdown(f'<div class="card">🎯 Your Challenge: **{challenge}**</div>', unsafe_allow_html=True)
        st.balloons()

    st.subheader("📚 Daily Reflection")
    reflection = st.text_area("What did you learn today? Write your thoughts below:")

    if st.button("📩 Submit Reflection"):
        st.success("Awesome! Keep reflecting and growing every day!")

    st.markdown('<div class="button">🔹 Keep Growing & Learning! 🔹</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
