# Python Data & Algorithmic Solutions

A comprehensive Python script designed to perform statistical analysis on a given dataset, integrate with a PostgreSQL database, and demonstrate fundamental programming algorithms. This project showcases skills in data manipulation, database management, and core computer science concepts.

## ✨ Features
- **Statistical Analysis**: Calculates mean, median, mode, variance, and probability from a sample color dataset.
- **Database Integration**: Connects to a PostgreSQL database, creates a table, and inserts the analyzed data for persistence.
- **Recursive Search**: Implements a recursive algorithm to efficiently search for an element within a list.
- **Fibonacci Sequence**: Generates the first 50 numbers of the Fibonacci sequence and calculates their sum.
- **Number Conversion**: Includes a utility for generating a random binary number and converting it to its base-10 equivalent.

## 🛠️ Technologies Used

| Technology | Description |
| :--- | :--- |
| [Python](https://www.python.org/) | Core programming language for the script's logic. |
| [Pandas](https://pandas.pydata.org/) | Used for potential data manipulation tasks (though minimally in the final script). |
| [NumPy](https://numpy.org/) | Provides support for numerical operations. |
| [PostgreSQL](https://www.postgresql.org/) | The relational database used for storing the analysis results. |
| [Psycopg2](https://www.psycopg.org/docs/) | A PostgreSQL database adapter for Python. |

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8 or newer
- Pip (Python package installer)
- A running instance of PostgreSQL

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Victormarshall911/python-interview.git
    ```

2.  **Navigate to the Project Directory**
    ```bash
    cd python-interview
    ```

3.  **Create and Activate a Virtual Environment** (Recommended)
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set Up PostgreSQL Database**
    - Ensure your PostgreSQL server is running.
    - Create a new database named `bincomdb`.
    - **Important**: Update the database connection credentials in the `solution.py` file to match your local setup.

    ```python
    # solution.py
    connection = psycopg2.connect(
        host="localhost",      # Your host
        database="bincomdb",   # Your database name
        user="postgres",       # Your PostgreSQL username
        password="itswell77"   # Your PostgreSQL password
    )
    ```

## Usage

Once the installation is complete and the database is configured, you can run the script from your terminal:

```bash
python solution.py
```

The script will execute the following tasks and print the results to the console:
1.  Perform statistical analysis on the hardcoded color data.
2.  Save the frequency of each color to your `bincomdb` database in a table named `color_frequency`.
3.  Prompt you to enter a number to test the recursive search function.
4.  Generate and display a random binary number and its decimal equivalent.
5.  Calculate and display the sum of the first 50 Fibonacci numbers.

### Expected Output

```
Color Frequency Table:
GREEN: 9
YELLOW: 4
BROWN: 5
...
ORANGE: 6
...

1. Mean color: BROWN
2. Most worn color: BLUE
3. Median color: RED
4. Variance of colors: 6.888888888888889
5. Probability of RED: 0.08

Data saved to PostgreSQL successfully.

Enter a number to search: 12
Found!

Generated Binary: 1011, Base-10: 11

Sum of first 50 Fibonacci numbers: 20365011073
```

## License

This project is not under a specific license. All rights are reserved.

---
<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

</div>
