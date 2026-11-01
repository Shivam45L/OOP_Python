<<<<<<< HEAD
# Health Insurance Premium Prediction

## Project structure
- `main.py` — FastAPI backend and model prediction
- `HI_model.pkl` — your existing trained model
- `templates/index.html` — HTML + Bootstrap form
- `static/style.css` — custom styling
- `requirements.txt` — Python dependencies

## Run on Windows (Anaconda Prompt or terminal)

1. Open the terminal in this project folder.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Start the FastAPI server:
   `uvicorn main:app --reload`
4. Open `http://127.0.0.1:8000` in your browser.

The interactive API docs are at `http://127.0.0.1:8000/docs`.

## Important
The backend keeps the same feature order and encoding as the supplied Streamlit code:
`[age, gender_enc, bmi, children, smoker_enc]`
where female = 1, male = 0, yes smoker = 1, and no smoker = 0.

Only load pickle files you trust. For consistent results, use a compatible scikit-learn version with the one used when the model was trained.
=======
# OOP_Python
>>>>>>> ba176c94d72c96c6d1360c6daae9d47a67858dc0
