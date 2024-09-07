# MNIST Digit Recognizer

This project is a web application that uses a machine learning model to recognize handwritten digits from the MNIST dataset. Users can upload an image of a handwritten digit, and the application will predict which digit it is.

## Features

- Upload images of handwritten digits
- Real-time prediction using a trained Random Forest model
- User-friendly web interface
- FastAPI backend for quick and efficient processing

## Technologies Used

- Python 3.7+
- FastAPI
- scikit-learn
- HTML/CSS/JavaScript
- Pillow (Python Imaging Library)

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/Elotmanix/mnist-digit-recognizer.git
   cd mnist-digit-recognizer
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install fastapi uvicorn scikit-learn pillow python-multipart
   ```

4. Train the model :
   ```
   python mnist_model.py
   ```

5. Start the FastAPI server:
   ```
   uvicorn app:app --reload
   ```

6. Open `static/index.html` in a web browser or serve it using a local HTTP server.

## Usage

1. Open the web interface in your browser.
2. Click on the "Choose Image" button and select an image of a handwritten digit.
3. The application will display the image and show the predicted digit.

## Project Structure

- `mnist_model.py`: Script to train the Random Forest model on the MNIST dataset.
- `app.py`: FastAPI application that serves the prediction endpoint.
- `static/index.html`: Web interface for the application.
- `mnist_model.pkl`: Trained model file (generated after running `mnist_model.py`).

## API Endpoint

- POST `/predict-image/`: Accepts an image file and returns the predicted digit.

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request


## Acknowledgements

- MNIST Dataset: http://yann.lecun.com/exdb/mnist/
- scikit-learn: https://scikit-learn.org/
- FastAPI: https://fastapi.tiangolo.com/
