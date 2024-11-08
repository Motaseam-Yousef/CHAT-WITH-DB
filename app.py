from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide SQL query as the response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

# Function to retrieve query from DB
def read_sql_query(query, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Load prompt from environment
prompt = os.getenv("PROMPT")

# Streamlit App Configuration
st.set_page_config(page_title="Gemini SQL Query Retriever", page_icon="🔍", layout="centered")
st.sidebar.title("💡 Gemini SQL Query Retriever")
st.sidebar.markdown("Use the Gemini model to transform natural language questions into precise SQL queries and retrieve data from your database effortlessly.")

# Header and Description
st.title("🔍 Gemini SQL Query Retriever")
st.markdown("This app allows you to ask natural language questions about your database, and it returns relevant SQL query results using Google's Gemini model.")

# Input area for user's question
st.text_input("Enter your question about the database:", key="input", placeholder="e.g., 'What was the total revenue in 2023?'")

# Button to submit the question
if st.button("Retrieve Data"):
    # Run the Gemini model to get SQL query response
    with st.spinner("Generating SQL query..."):
        response_sql = get_gemini_response(st.session_state.input, prompt)
    
    # Display generated SQL query
    st.subheader("Generated SQL Query")
    st.code(response_sql, language="sql")
    
    # Execute SQL query on database
    try:
        with st.spinner("Retrieving data from database..."):
            response_data = read_sql_query(response_sql, "sqlite.db")
        
        # Display data if available
        if response_data:
            st.subheader("Query Results")
            st.write("Below are the results for your query:")
            st.table(response_data)  # Display results as a table
        else:
            st.warning("No data found for the given query.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.sidebar.markdown("### Powered by:")
st.sidebar.markdown("- Google Gemini Model")
st.sidebar.markdown("- Streamlit")
st.sidebar.markdown("- SQLite Database")

st.sidebar.info("Ensure the `GOOGLE_API_KEY` and `PROMPT` environment variables are set correctly for optimal performance.")
