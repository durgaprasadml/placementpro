# PlacementPro (Django)

PlacementPro is a role-based placement management web app with modules for Students, TPOs, and Alumni.

## Features
- Authentication: register/login/logout with role-based redirection.
- Student dashboard: profile, eligible drives, application tracker.
- Drive criteria engine: CGPA + branch + backlogs eligibility.
- Applications: status lifecycle (Applied → Aptitude Cleared → Interview Scheduled → Selected).
- Resume generator: downloadable PDF via ReportLab.
- Alumni referrals: alumni can post referrals; students can view referral feed.

## Tech Stack
- Django
- SQLite
- Bootstrap 5
- ReportLab

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install django reportlab
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Login: `http://127.0.0.1:8000/`
- Register: `http://127.0.0.1:8000/register/`
- Admin: `http://127.0.0.1:8000/admin/`

## How your team members can access it

### Option 1: Same Wi-Fi / LAN (quick internal sharing)
1. Run Django on all interfaces:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
2. Find your machine IP:
   - Linux/macOS: `ip a` or `ifconfig`
   - Windows: `ipconfig`
3. Teammates open:
   - `http://<your-ip>:8000/`

> If needed, allow inbound TCP `8000` in your firewall.

### Option 2: Temporary public access (without full deployment)
Use a tunnel service (example: ngrok or Cloudflare Tunnel):
```bash
# after running Django locally on port 8000
ngrok http 8000
```
Share the generated public URL with teammates.

### Option 3: Proper team access via deployment (recommended)
Deploy on a cloud platform (Render/Railway/Heroku/AWS) and share the hosted URL.
At minimum for production:
- Use PostgreSQL instead of SQLite.
- Set `DEBUG=False` and a secure `SECRET_KEY`.
- Configure `ALLOWED_HOSTS` with your domain.
- Serve static files properly (Whitenoise or object storage/CDN).
- Keep credentials in environment variables.
