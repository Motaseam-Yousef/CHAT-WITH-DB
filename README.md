# Gemini SQL Query Retriever

This application uses Google's Gemini model to transform natural language questions into precise SQL queries and retrieve data from a SQLite database. The app is built with Streamlit and provides a user-friendly interface for querying data.

## Features

- **Natural Language Queries**: Input your questions in plain English, and the app generates the corresponding SQL query.
- **SQL Query Display**: View the generated SQL query before executing it on the database.
- **Data Retrieval**: The app retrieves data from a SQLite database based on the generated SQL query.
- **User-Friendly Interface**: Built with Streamlit for a clean and accessible user experience.

## Getting Started

### Prerequisites

- Python 3.x
- [Streamlit](https://streamlit.io/)
- [SQLite](https://www.sqlite.org/index.html)
- A valid Google API Key with access to Google's Gemini model

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/gemini-sql-query-retriever.git
   cd gemini-sql-query-retriever
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   Create a `.env` file in the project root directory with the following keys:
   ```plaintext
   GOOGLE_API_KEY=your_google_api_key
   PROMPT="Your prompt for the Gemini model"
   ```

4. **Prepare the SQLite database**:
   
   Ensure you have a `sqlite.db` file in the root directory. Modify the database structure and data as needed.

### Running the Application

To start the Streamlit application, run:
```bash
streamlit run app.py
```

## Usage

1. **Enter a Question**: In the input box, type a question about the data in natural language (e.g., "What was the total revenue in 2023?").
2. **View Generated SQL Query**: The app displays the SQL query generated by the Gemini model.
3. **Retrieve Data**: The app executes the SQL query on the SQLite database and displays the results.

## Project Structure

```plaintext
├── app.py                 # Main Streamlit application
├── README.md              # Project documentation
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
└── sqlite.db              # SQLite database file
```

## Example Usage

- **Question**: "How many records are present?"
- **Generated SQL**: `SELECT COUNT(*) FROM sales_data;`
- **Query Result**: Displays the count of records in the `sales_data` table.

## Error Handling

The app includes error handling to manage issues during the query execution. If the query fails, an error message will appear, indicating the issue.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Google Gemini Model](https://cloud.google.com/generative-ai)
- [Streamlit](https://streamlit.io/)
- [SQLite](https://www.sqlite.org/index.html)

Enjoy querying your data with ease using natural language and Streamlit!