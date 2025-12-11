import streamlit as st
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyBirq4lKZ5pLHhSE6yh92tfctwB-ztVr9k")

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_response(prompt, max_length=300, temperature=0.2, topp=0.7):
    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "max_output_tokens": max_length,
                "temperature": temperature,
                "top_p": topp,
            }
        )
        return response.text

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None


# Streamlit UI
st.title("Prompt Engineering with Gemini API")
st.write("Enter your prompt below and see the Gemini model response.")

user_prompt = st.text_area("Prompt", height=200)

if st.button("Generate Response"):
    if user_prompt:
        with st.spinner("Generating response..."):
            output = generate_response(user_prompt)
            if output:
                st.subheader("Gemini's Response:")
                st.write(output)
    else:
        st.warning("Please enter a prompt before generating a response.")

st.write("This app uses Google Gemini API to generate responses.")
