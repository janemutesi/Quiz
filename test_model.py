import pickle

# Load the saved model
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    print("Model loaded successfully!")

    # Test the model with a sample input
    sample_input = [[50, 3]]  # Example: 50 square meters, 3 rooms
    prediction = model.predict(sample_input)
    print(f"Prediction for input {sample_input}: {prediction[0]}")

except Exception as e:
    print(f"Error loading model: {e}")
