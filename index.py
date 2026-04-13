from backend.Main import app

# Vercel Python runtime detects the Flask app object exported here.
# Also export the common WSGI variable for compatibility.
application = app
