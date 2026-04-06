# ⛓ ChainVote — Setup Guide (Windows)

## Step 1 — Install Python
Download Python 3.11+ from https://python.org/downloads
During install, check "Add Python to PATH"

## Step 2 — Open Command Prompt
Press Win + R → type `cmd` → Enter
Navigate to your desired folder:
```
cd C:\Users\YourName\Desktop
```

## Step 3 — Extract the zip
Unzip `chainvote.zip` here. You'll get a `chainvote` folder.
```
cd chainvote
```

## Step 4 — Create a virtual environment
```
python -m venv env
env\Scripts\activate
```
You'll see `(env)` at the start of your prompt. 

## Step 5 — Install dependencies
```
pip install -r requirements.txt
```

## Step 6 — Set up the database
```
python manage.py migrate
```

## Step 7 — Seed sample data (elections + test users)
```
python manage.py seed_data
```
This creates:
-  Admin: username=`admin`  password=`admin123`
-  Voter: username=`voter1` password=`voter123`
- 3 sample elections (1 active, 1 upcoming, 1 ended)

## Step 8 — Run the server
```
python manage.py runserver
```

## Step 9 — Open in browser
| URL | Purpose |
|-----|---------|
| http://127.0.0.1:8000/ | Main app |
| http://127.0.0.1:8000/admin/ | Django admin panel |
| http://127.0.0.1:8000/api/elections/ | REST API |

---

## REST API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/elections/ | List all elections |
| GET | /api/elections/<id>/ | Election detail |
| POST | /api/elections/<id>/vote/ | Cast a vote (auth required) |
| GET | /api/elections/<id>/results/ | Get results |

---

## Common Issues

**"python not recognized"** → Reinstall Python and check "Add to PATH"

**"No module named django"** → Make sure your virtualenv is activated (`env\Scripts\activate`)

**Port already in use** → Run on a different port: `python manage.py runserver 8080`
