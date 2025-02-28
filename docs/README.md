# Project Documentation

## Project Overview
This project is a chat application that utilizes the Ollama model for generating responses based on user input. It integrates with Pinecone for vector storage and retrieval of information.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```bash
python app.py
```
The application will be accessible at `http://localhost:3342`.

### API Endpoints
- **GET /**: Renders the chat interface.
- **POST /ask**: Sends a message to the model and retrieves a response.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License.
