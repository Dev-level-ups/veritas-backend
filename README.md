# Veritas Backend

Backend API for Veritas, built with **FastAPI** and **Supabase**.

## Table of Contents

- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Running the Server](#running-the-server)
- [API Documentation](#api-documentation)
- [Security Notes](#security-notes)

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/): web framework
- [Uvicorn](https://www.uvicorn.org/): ASGI server
- [Supabase](https://supabase.com/): database and backend services

## Project Structure

```
veritas-backend/
│
├── app/
│   └── routes/
│       └── documents.py      # Document-related API routes
│
├── main.py                   # Application entry point
├── supabase_client.py        # Supabase client setup
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not committed)
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.9 or higher
- pip
- A Supabase project (URL and secret key)

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd veritas-backend
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root (see [Environment Variables](#environment-variables)).

### 5. Start the development server

```bash
python -m uvicorn main:app --reload
```

## Environment Variables

Create a `.env` file in the project root with the following:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_secret_key
```

| Variable       | Description                        |
| -------------- | ---------------------------------- |
| `SUPABASE_URL` | Your Supabase project URL          |
| `SUPABASE_KEY` | Your Supabase secret (service) key |

## Running the Server

Start the development server with auto-reload:

```bash
python -m uvicorn main:app --reload
```

The API will be available at: <http://127.0.0.1:8000>

## Security Notes

- **Do not commit `.env`** to version control. Make sure it is listed in `.gitignore`.
- **Never expose your Supabase secret key** in client-side code, logs, or public repositories.