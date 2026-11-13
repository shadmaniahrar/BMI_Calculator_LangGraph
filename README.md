# BMI_Calculator_LangGraph
    
A stateful BMI calculator web application built with LangGraph and Streamlit, deployed on Streamlit. 

A stateful BMI Calculator web application built using Python, LangGraph, and Streamlit. This project demonstrates graph-based workflow orchestration, state management, BMI calculation, and interactive web application development.

🚀 Project Overview

The application allows users to enter their height and weight to calculate their Body Mass Index (BMI).

It uses LangGraph to manage the application workflow through different processing nodes and Streamlit to provide an interactive user interface.

The project demonstrates how stateful workflows can be designed and executed using LangGraph.

✨ Key Features

- BMI calculation using height and weight.
- Stateful workflow management using LangGraph.
- Graph-based execution with nodes and edges.
- BMI category classification.
- Interactive web interface using Streamlit.
- Input processing and validation.
- Cloud deployment using Streamlit Community Cloud.

🛠️ Technologies Used

Technology| Purpose
Python| Core programming
LangGraph| Stateful workflow orchestration
Streamlit| Frontend and web interface
Git| Version control
GitHub| Source code management
Streamlit Community Cloud| Application deployment

⚙️ LangGraph Workflow Architecture

The application follows a graph-based workflow:

       User Input
           |
           v
   Input Processing Node
           |
           v
    BMI Calculation Node
           |
           v
   BMI Classification Node
           |
           v
    Result Generation Node
           |
           v
      Final Output
           |
           v
      Streamlit UI

Workflow Explanation

1. User Input: Accepts height and weight from the user.

2. Input Processing: Validates and processes the input.

3. BMI Calculation: Calculates BMI using the formula:
   
   BMI = Weight (kg) / Height (m)²

4. BMI Classification: Determines the BMI category.

5. Result Generation: Prepares the final calculation and interpretation.

6. State Management: LangGraph manages the workflow state and execution.

7. Final Output: Streamlit displays the result.

📊 BMI Categories

BMI Range| Category
Below 18.5| Underweight
18.5–24.9| Normal Weight
25–29.9| Overweight
30 or above| Obesity

BMI categories are general adult screening guidelines and are not a medical diagnosis.

📁 Project Structure

BMI_Calculator_LangGraph/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── Other project files

💻 Installation and Local Setup

Step 1: Clone the Repository

git clone https://github.com/shadmaniahrar/BMI_Calculator_LangGraph.git

Step 2: Navigate to the Project

cd BMI_Calculator_LangGraph

Step 3: Create a Virtual Environment

python -m venv venv

Activate on Windows:

venv\Scripts\activate

Step 4: Install Dependencies

pip install -r requirements.txt

Step 5: Run the Application

streamlit run app.py

The application will open in your browser.

☁️ Deployment – Streamlit Community Cloud

The application can be deployed using Streamlit Community Cloud.

Deployment steps:

1. Push the project code to GitHub.
2. Visit https://share.streamlit.io/
3. Sign in using your GitHub account.
4. Click Create app.
5. Select the "BMI_Calculator_LangGraph" repository.
6. Select the deployment branch ("main").
7. Enter the main application file path ("app.py").
8. Click Deploy.

Streamlit Community Cloud will install the dependencies from "requirements.txt" and deploy the application.

🎯 Learning Outcomes

- Understanding LangGraph architecture.
- Building stateful workflows.
- Working with graph nodes and edges.
- Managing application state.
- Integrating LangGraph with Streamlit.
- Developing interactive Python applications.
- Deploying Python applications using Streamlit Community Cloud.
- Managing source code using Git and GitHub.

🔮 Future Enhancements

- BMI history tracking.
- Interactive BMI charts and visualizations.
- Improved user experience.
- Additional health-related insights.
- LLM-powered conversational explanations.

👩‍💻 Author

Shadmani Ahrar Mundari

GitHub: https://github.com/shadmaniahrar

---

⭐ If you find this project useful, feel free to explore the repository.

Disclaimer: This application is developed for educational purposes and general BMI estimation. It is not a substitute for professional medical advice
