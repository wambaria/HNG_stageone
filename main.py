from fastapi import FastAPI, Query
from datetime import datetime, timedelta
import pytz

app = FastAPI()

@app.get("/app")
async def root(
    slack_name: str = Query(""),
    track: str = Query("")
):

    current_day = datetime.now().strftime("%A")
    utc_time = utc_time + timedelta(hours=2)
    utc_time = utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url":
        "github_repo_url":
        "status_code": 200
    }

    return response_data

if __name__ == "__main__":
    import uvicorn