# Vercel Serverless API

This directory contains serverless functions for Vercel deployment.

## Files

- `index.py` - Main API handler for Vercel

## Endpoints

When deployed to Vercel, the following endpoints are available:

### POST /api/chat
Chat with KawaiiGPT

**Request Body:**
```json
{
  "message": "Your message here"
}
```

**Response:**
```json
{
  "response": "AI response",
  "model": "kawaii-3-amp"
}
```

### GET /api/health
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "service": "KawaiiGPT-Vercel",
  "version": "K2.5-Latest:301025"
}
```

## Local Testing

To test serverless functions locally:

```bash
vercel dev
```

This will start a local development server at `http://localhost:3000`
