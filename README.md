# Contact Form API 

This project is a serverless backend API for processing contact form submissions. It is built with:

- AWS Lambda (Python)
- API Gateway (REST)
- DynamoDB (NoSQL database)
- AWS SAM (Serverless Application Model) for infrastructure as code

This API accepts 'POST' requests with contact details and stores them securely in a DynamoDB table.

---

## Features

- Accepts JSON POST requests with 'name', 'email', and 'message'
- Stores each message in a DynamoDB table with a unique identifier and timestamp
- Fully serverless and scalable
- Deployable using AWS SAM CLI

---

## Architecture

Client → API Gateway → Lambda Function → DynamoDB

---

## Project Structure

```text
.
├── contact_handler/
│   ├── __init__.py
│   └── app.py
├── events/ 
├── tests/ 
├── template.yaml
├── README.md
├── .gitignore
└── LICENSE
```  

---

## Prerequisites

To run and deploy this project, you need:

- Python 3.10
- AWS CLI configured with access to your AWS account
- AWS SAM CLI installed
- Git (for version control and deployment to GitHub)

---

## Installation and Deployment

### 1. Clone the repository
```bash
git clone https://github.com/your-username/contact-form-api.git
cd contact-form-api
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows
```

### 3. Install dependencies
```bash
pip install boto3
```

### 4. Build the application
```bash
sam build
```

### 5. Deploy to AWS
```bash
sam deploy --guided
```

Follow the prompts. AWS SAM will package and deploy the Lambda function, API Gateway, and DynamoDB table. The deployed API endpoint will be displayed at the end of the process.

---

## Example API Request

### Method: POST

#### URL:
```text 
https://kevk5pd6f4.execute-api.eu-west-3.amazonaws.com/Prod/form
```

#### Headers:
```bash
Content-Type: application/json
```

#### Body (JSON):
```bash
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Hello, this is a test message."
}
```

#### Response:

- Success (200 OK):
```bash
{
  "message": "Message received successfully!"
}
```

- Error (400 Bad Request):
```bash
{
  "error": "Missing name, email, or message"
}
```

- Error (500 Internal Server Error):
```bash
{
  "error": "Error message details"
}
```

---

## Future Improvements
- Add email validation using regex to improve input quality
- Implement unit tests for the Lambda function to ensure reliability
- Store form submissions in Amazon S3 as a backup solution
- Configure CORS to enable frontend integration
- Add basic logging to Lambda for better monitoring and debugging
- Develop a simple static frontend hosted on S3 to submit the contact form

---

## License
This project is licensed under the [MIT License](LICENSE).