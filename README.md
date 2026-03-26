# Final Project 

This project is an **Emotion Detection Web Application** built in Python that uses IBM Watson NLP services to analyze text and identify human emotions. The system takes user input text and returns emotion scores for five categories: **anger, disgust, fear, joy, and sadness**, along with the **dominant emotion** based on the highest score. The main goal of the project is to demonstrate how natural language processing (NLP) and machine learning–based APIs can be integrated into a simple but functional web application.

The core functionality is implemented in a Python module called `emotion_detection.py`, which sends requests to the Watson Emotion Prediction API and processes the JSON response into a structured format. The application also includes a Flask-based web server (`server.py`) that exposes an endpoint allowing users to submit text through a browser and receive real-time emotion analysis results. This makes the tool accessible as a lightweight web service.

To ensure reliability, the project includes **unit testing** using Python’s `unittest` framework, which validates that the emotion detection function returns correct outputs for different inputs. Additionally, the application implements **error handling** to manage cases such as empty user input or failed API responses, ensuring the system does not crash and always returns a meaningful response.

The project is structured as a proper Python package using an `__init__.py` file, making it modular and reusable. It also includes **static code analysis using pylint**, which helps maintain code quality and readability by identifying potential issues and enforcing best practices. Finally, the application is deployed locally through Flask, allowing users to test the system in a browser via a simple URL query.

Overall, this project demonstrates key software engineering concepts such as API integration, modular design, testing, error handling, and web deployment, while showcasing how AI-powered emotion detection can be applied in real-world applications.
