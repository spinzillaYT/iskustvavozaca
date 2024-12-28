# Car Search Application

This is a web application for searching and filtering cars based on various criteria such as brand, model, engine type, and power.

## Features

- Search cars by brand, model, and year
- Filter by engine type (benzin, dizel, hibrid, elektro)
- Filter by engine power range
- Modern and responsive user interface
- Real-time search results

## Installation

1. Make sure you have Python 3.7+ installed on your system

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Populate the database with initial car data:
```bash
python populate_db.py
```

4. Run the application:
```bash
python app.py
```

5. Open your web browser and navigate to:
```
http://localhost:5000
```

## Database Structure

The application uses SQLite with the following structure:

- Brands (name)
- Models (name, year_start, year_end, brand_id)
- Engines (type, displacement, power, model_id)

## Technology Stack

- Backend: Flask, SQLAlchemy
- Frontend: HTML5, CSS3, JavaScript
- UI Framework: Bootstrap 5
- Database: SQLite
