# QUIZ  
*REG: 24RP14525*  
*Model-Deployment*

This project provides a step-by-step guide on how to deploy a machine learning model using a pickle file with two different methods:

1. *Gradio UI* (gradio_app.py) - A graphical interface that accepts inputs, processes the request locally, and displays the prediction.  
2. *Flask API* (app.py) - A backend API that receives requests via a Flask form or Postman, processes the data, and returns a prediction.



## Project Structure


/ML-QUIZ
│── Templates/           # HTML templates used by Flask
│   │── home.html
│   │── index.html  
│── app.py               # Flask API for predictions
│── gradio_app.py        # Gradio UI for local predictions
│── model.pkl            # Pre-trained machine learning model (Pickle file)
│── requirements.txt     # Required dependencies

![image](https://github.com/user-attachments/assets/90f31b00-0d2a-43cd-a892-502149e727de)



## Running Process

# 1. Set Up Virtual Environment
Create and activate a virtual environment:

 Create virtual environment
 # python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

![image](https://github.com/user-attachments/assets/1d3efb43-ee03-4c93-ba61-fb68e76a8375)

### 2. Install Dependencies
Install the required Python packages:

pip install -r requirements.txt

## Running the Applications

1. Running the Flask API (app.py)
Start the Flask application:


# python3 app.py
- The Flask app will run on http://127.0.0.1:5000/.
- Access the frontend form at http://127.0.0.1:5000/.
![image](https://github.com/user-attachments/assets/d5dbc5d9-7d22-4a9d-bbf9-99ae91911f48)

#### API Endpoint
- *URL*: http://127.0.0.1:5000/price
- *Method*: POST

#### Using Postman to Send a Request
1. Open Postman.
2. Set the method to POST.
3. Use the URL: http://127.0.0.1:5000/price.
4. Send JSON data in the body:

   json
   {
     "area": 300,
     "room": 10
   }
   

#### Example Response
json
{
  "predicted_price": 3.9
}


![image](https://github.com/user-attachments/assets/c490c435-203e-4ba5-8393-651449a47b54)


### 2. Running the Gradio UI (gradio_app.py)
Start the Gradio application:


python gradio_app.py


- The Gradio app will run on http://127.0.0.1:7860/.
- Open the URL in your browser to access the Gradio interface.

#### Features
- Accepts area and room as inputs.
- Uses a local prediction function instead of an API.
- Displays the predicted house price.


## Additional Description

### app.py (Flask API)
- Loads the model.pkl file.
- Creates an API endpoint /price that accepts POST requests.
- Accepts area and room as input and returns the predicted price.
- Supports requests from both Postman and a Flask form.

### gradio_app.py (Gradio UI)
- Provides a graphical interface for users to input area and room.
- Uses a dummy formula to predict house prices.
- No API calls—everything is processed locally.
- Runs on http://127.0.0.1:7860/.



## Features
- *Gradio UI*: Simple and interactive interface for local predictions.
- *Flask API*: Scalable backend for integrating predictions into other applications.
- *Postman Support*: Easily test the API endpoint using Postman.




