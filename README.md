# Image Moderation FastAPI

## Setup

1. Add `.env` with the MONGO_URI as needed
2. Build and run with Docker Compose:

   ```
   docker-compose up --build
   ```

3. Backend: [http://localhost:7000/docs](http://localhost:7000/docs)
4. Frontend: [http://localhost:8000](http://localhost:8000)

## API

- All endpoints require `Authorization: Bearer <token>`.
- Admin endpoints: `/auth/tokens` (POST, GET, DELETE)
- Moderation endpoint: `/moderate` (POST, image upload)

## Notes

- This current implementation uses dummy moderation logic.
<!-- - Testing auth token: E0aWmcwL_MqUAEIm0Ug-PqveUMqIPlYImiFLO2ms7VA -->