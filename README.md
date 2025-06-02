
# FastAPI-For-ML-Projects

 A hands-on learning repository for building and deploying Machine Learning models using **FastAPI**.

## 📚 Purpose

This repository is created for educational purposes to explore how to:

- Build REST APIs with FastAPI
- Integrate Machine Learning models into APIs
- Serve ML models efficiently
- Handle data input/output validation using Pydantic
- Test and document endpoints
- Explore deployment options

##  What You'll Learn

- FastAPI basics (routes, async, request/response models)
- Loading and using ML models with FastAPI
- Creating POST and GET endpoints
- Using `pydantic` for input validation
- Testing APIs with Swagger UI and Postman


##  Getting Started

```bash
# Clone the repo
git clone https://github.com/yourusername/FastAPI-For-ML-Projects.git
cd FastAPI-For-ML-Projects

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn app.main:app --reload
```


##  Tech Stack

- **FastAPI** – API Framework  
- **Scikit-learn / XGBoost / Pickle** – ML Models  
- **Pydantic** – Data validation  
- **Uvicorn** – ASGI server  

## Notes

This repository is intended for **learning and experimentation only**.  
