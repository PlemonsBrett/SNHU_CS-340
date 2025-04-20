# Grazioso Salvare Dashboard

A modern dashboard application for Grazioso Salvare to identify potential search-and-rescue dogs from animal shelter data.

## Project Overview

Grazioso Salvare identifies dogs that are good candidates for search-and-rescue training. This dashboard application helps them interact with animal shelter data to find dogs suitable for different types of rescue operations:

- Water Rescue
- Mountain or Wilderness Rescue
- Disaster Rescue or Individual Tracking

The application provides an intuitive interface for filtering, visualizing, and exploring animal shelter records.

## Features

- Interactive filtering by rescue type
- Responsive data table with sorting and filtering capabilities
- Geolocation map showing where animals were found
- Pie chart visualization of breed distribution
- Modern, user-friendly interface with Bootstrap styling

## Technology Stack

- **Backend**: Python, MongoDB, PyMongo
- **Frontend**: Dash, Plotly, Dash Bootstrap Components, Dash Leaflet
- **Development**: Poetry, Pyright, Ruff, Pydantic

## Installation

### Prerequisites

- Python 3.12 or higher
- MongoDB (running locally or accessible remotely)
- The Austin Animal Center Outcomes dataset imported into MongoDB

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/grazioso-salvare.git
   cd grazioso-salvare
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Add the Grazioso Salvare logo:
   - Place the logo file in `src/grazioso/dashboard/assets/grazioso_salvare_logo.png`

4. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Usage

### Running the Dashboard

Start the dashboard application:

```bash
poetry run dashboard
```

Or, from within an activated Poetry shell:

```bash
dashboard
```

The dashboard will be available at `http://localhost:8050` in your web browser.

### Dashboard Interface

The dashboard interface consists of:

1. **Header** - Grazioso Salvare branding and author information
2. **Filter Controls** - Radio buttons to filter by rescue type
3. **Data Table** - Interactive table showing filtered animal records
4. **Map** - Geolocation map showing the location of the selected animal
5. **Pie Chart** - Distribution of top 10 breeds in the current filter

### Filtering Data

Select one of the rescue type options:
- **All Dogs** - Shows all dogs in the database
- **Water Rescue** - Shows dogs suitable for water rescue operations
- **Mountain or Wilderness Rescue** - Shows dogs suitable for mountain rescue operations
- **Disaster Rescue or Individual Tracking** - Shows dogs suitable for disaster rescue operations

The data table, map, and pie chart will update automatically based on your selection.

## Development

### Project Structure

```
grazioso-salvare/
├── src/
│   └── grazioso/
│       ├── __init__.py
│       ├── crud.py           # CRUD operations for MongoDB
│       ├── models.py         # Pydantic data models
│       ├── scripts.py        # CLI scripts
│       └── dashboard/        # Dashboard application
│           ├── __init__.py
│           ├── app.py        # Main application
│           ├── settings.py   # Application settings
│           ├── layouts.py    # Dashboard layouts
│           ├── callbacks.py  # Dash callbacks
│           ├── utils.py      # Utility functions
│           ├── assets/       # Static assets
│           └── components/   # Dashboard components
├── notebooks/               # Jupyter notebooks
├── tests/                   # Test files
├── pyproject.toml           # Poetry configuration
└── README.md
```

### Development Commands

- Format code: `poetry run format`
- Lint code: `poetry run lint`
- Type checking: `poetry run typecheck`
- Run dashboard in debug mode: `poetry run dashboard --debug`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Authors

- Brett Plemons

## Acknowledgments

- SNHU CS-340 Client/Server Development course
- Grazioso Salvare (fictional client)
- Austin Animal Center for the dataset
