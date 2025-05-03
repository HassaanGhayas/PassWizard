import streamlit as st
import string
from random import choice

# --- Functions ---

def generate_password(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(choice(characters) for _ in range(length))

def check_password_strength(password: str) -> tuple[int, list[str]]:
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Password length should be at least 8 characters.")

    if any(i.islower() for i in password) and any(i.isupper() for i in password):
        score += 2
    else:
        suggestions.append("Include both uppercase and lowercase letters.")

    if any(i.isdigit() for i in password) and any(i in string.punctuation for i in password):
        score += 2
    else:
        suggestions.append("Include at least one digit and one special character.")

    return score, suggestions


# --- Streamlit UI ---

st.set_page_config(page_title="Password Tools", page_icon="🔐")
st.title(":red[Pass]:violet[Wizard] 🪄")

tabs = st.tabs(["🔍 Check Strength", "⚙️ Generate Password"])


# --- Password Strength Checker ---
with tabs[0]:
    st.subheader("Check Password Strength")

    password = st.text_input("Enter your password", type="password")

    if st.button("Check Strength", "strength_checking"):
        if password:
            score, tips = check_password_strength(password)
            st.subheader(f"Password Score: {score}/6")

            if score == 6:
                st.success("✅ Your password is strong!")
            else:
                st.warning("⚠️ Your password could be improved:")
                for tip in tips:
                    st.markdown(f"- {tip}")
        else:
            st.error("Please enter a password to check.")


# --- Password Generator ---
with tabs[1]:
    st.subheader("Generate a Strong Password")

    length = st.slider("Select password length", min_value=8, max_value=32, value=12)

    if st.button("Generate Password", "password_generate"):
        generated = generate_password(length)
        st.code(generated, language="text")
        st.success("✅ Copy and use your strong password!")
