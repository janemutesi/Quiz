from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load your trained model (Ensure the file exists)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')  # Render the form page

@app.route('/price', methods=['POST'])
def predict():
    try:
        # Get JSON data from the frontend
        data = request.get_json()

        # Extract input values
        area = float(data['area'])
        room = float(data['room'])

        # Make a prediction
        prediction = float(model.predict([[room, area]])[0])

        # Return JSON response
        return jsonify({'predicted_price': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
