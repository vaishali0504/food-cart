# 🍔 Food Cart — Railway Deployment Guide

## Local Development
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Local uses SQLite automatically ✅

---

## Deploy to Railway

### Step 1 — Push to GitHub
```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/YOUR_USERNAME/food-cart.git
git push -u origin main
```

### Step 2 — Create Railway Project
1. Go to railway.app → Login with GitHub
2. Click "New Project" → "Deploy from GitHub repo"
3. Select this repository

### Step 3 — Add PostgreSQL Database
Inside Railway project → Click "+ New" → "Database" → "PostgreSQL"
Railway auto-sets DATABASE_URL ✅

### Step 4 — Set Environment Variables
Go to Django service → Variables tab → Add:
```
SECRET_KEY = your-new-secret-key
DEBUG = False
ALLOWED_HOSTS = yourapp.up.railway.app
```

Generate SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5 — Generate Domain
Settings tab → Domains → Generate Domain → Done! 🎉

## Note on Media Files
Railway does not permanently store uploaded images.
For production uploads, use Cloudinary (free tier available).
