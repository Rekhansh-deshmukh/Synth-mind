# Installation Instructions

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation Steps
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add the following:
   ```
   PINECONE_API_KEY=<your-pinecone-api-key>
   ```

5. **Run the application**:
   ```bash
   python app.py
