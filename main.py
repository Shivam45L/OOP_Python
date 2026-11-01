from pathlib import Path
import pickle

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "HI_model.pkl"

# Load the trained model once when the application starts.
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

app = FastAPI(title="Health Insurance Premium Prediction")

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"prediction": None, "error": None, "form": {}},
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    age: int = Form(...),
    gender: str = Form(...),
    bmi: float = Form(...),
    children: int = Form(...),
    smoker: str = Form(...),
):
    form = {
        "age": age,
        "gender": gender,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
    }

    prediction = None
    error = None

    # Basic validation before sending values to the model.
    if not 0 <= age <= 120:
        error = "Please enter an age between 0 and 120."
    elif bmi <= 0:
        error = "BMI must be greater than 0."
    elif children < 0:
        error = "Number of children cannot be negative."
    elif gender not in ("female", "male"):
        error = "Please select a valid gender."
    elif smoker not in ("yes", "no"):
        error = "Please select a valid smoking status."
    else:
        # Keep the same encoding and feature order as your Streamlit app.
        gender_enc = 1 if gender == "female" else 0
        smoker_enc = 1 if smoker == "yes" else 0
        input_data = [[age, gender_enc, bmi, children, smoker_enc]]

        try:
            prediction = round(float(model.predict(input_data)[0]), 2)
        except Exception:
            error = (
                "Prediction failed. Check that this input order and encoding "
                "match the model you trained."
            )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"prediction": prediction, "error": error, "form": form},
    )
