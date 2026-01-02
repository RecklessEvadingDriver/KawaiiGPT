# KawaiiGPT Deployment Guide

This guide explains how to deploy KawaiiGPT on various hosting platforms.

## Table of Contents
- [Heroku Deployment](#heroku-deployment)
- [Vercel Deployment](#vercel-deployment)
- [Local Web Server](#local-web-server)

---

## Heroku Deployment

### Prerequisites
- [Heroku account](https://signup.heroku.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed

### Quick Deploy
Click the button below to deploy directly to Heroku:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Manual Deployment Steps

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create a new Heroku app**
   ```bash
   heroku create your-kawaiigpt-app
   ```

3. **Set environment variables** (optional)
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   ```

4. **Deploy the application**
   ```bash
   git push heroku main
   ```

5. **Open your app**
   ```bash
   heroku open
   ```

### Configuration Files
- `Procfile` - Defines how Heroku should run the application
- `runtime.txt` - Specifies Python version
- `app.json` - App metadata and configuration
- `requirements.txt` - Python dependencies

### Environment Variables
- `SECRET_KEY` - Flask session secret (auto-generated)
- `DEBUG` - Debug mode (default: False)
- `PORT` - Port number (auto-assigned by Heroku)

---

## Vercel Deployment

### Prerequisites
- [Vercel account](https://vercel.com/signup)
- [Vercel CLI](https://vercel.com/download) (optional)

### Quick Deploy
Click the button below to deploy directly to Vercel:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/RecklessEvadingDriver/KawaiiGPT)

### Manual Deployment Steps

1. **Install Vercel CLI** (if not already installed)
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy the application**
   ```bash
   vercel
   ```

4. **For production deployment**
   ```bash
   vercel --prod
   ```

### Configuration Files
- `vercel.json` - Vercel configuration and routing
- `api/index.py` - Serverless API functions

### API Endpoints (Vercel)
- `/api/chat` - Chat endpoint (POST)
- `/api/health` - Health check (GET)

---

## Local Web Server

### Running Locally

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask application**
   ```bash
   python app.py
   ```

3. **Access the application**
   Open your browser and navigate to: `http://localhost:5000`

### Development Mode
To run in development mode with auto-reload:
```bash
export DEBUG=True
python app.py
```

Or on Windows:
```cmd
set DEBUG=True
python app.py
```

---

## Architecture Overview

### Web Interface
- **Frontend**: HTML/CSS/JavaScript (single-page application)
- **Backend**: Flask web server
- **API**: RESTful endpoints for chat functionality

### Deployment Structure
```
KawaiiGPT/
├── app.py                  # Main Flask application (Heroku)
├── api/
│   └── index.py           # Vercel serverless functions
├── templates/
│   └── index.html         # Web interface
├── Procfile               # Heroku process definition
├── runtime.txt            # Python version for Heroku
├── app.json               # Heroku app configuration
├── vercel.json            # Vercel configuration
└── requirements.txt       # Python dependencies
```

---

## Troubleshooting

### Heroku Issues

**Problem**: Application crashes on startup
- **Solution**: Check logs with `heroku logs --tail`
- Ensure all dependencies are in `requirements.txt`
- Verify Python version in `runtime.txt` is supported

**Problem**: Port binding error
- **Solution**: Ensure app uses `PORT` environment variable:
  ```python
  PORT = int(os.environ.get('PORT', 5000))
  ```

### Vercel Issues

**Problem**: API endpoints not working
- **Solution**: Ensure `vercel.json` routing is correct
- Check that serverless functions are in the `api/` directory

**Problem**: Build fails
- **Solution**: Check Python version compatibility
- Verify all dependencies are compatible with Vercel's Python runtime

---

## Features in Web Version

✨ **Available Features**:
- Web-based chat interface
- Session management
- RESTful API endpoints
- Health monitoring
- Mobile-responsive design

🚧 **Coming Soon**:
- Image generation support
- Advanced model selection
- User authentication
- Conversation history persistence

---

## Support

For issues and questions:
- Check the [GitHub Issues](https://github.com/RecklessEvadingDriver/KawaiiGPT/issues)
- Join our [Telegram community](https://t.me/kawaiigpt_official)

---

## License

This project is open source. See LICENSE file for details.

Made with 🔥 by AI Empower Team
