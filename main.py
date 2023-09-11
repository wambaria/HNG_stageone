from fastapi import FastAPI, Query
from datetime import datetime, timedelta
import pytz

app = FastAPI()

@app.get("")
async def root(
    slack_name: str = Query(""),
    track: str = Query("")
):

    current_day = datetime.now().strftime("%A")
    utc_time = utc_time + timedelta(hours=2)
    utc_time = utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    github_file_url = "https://github.com/wambaria/HNG_stageone/blob/main/main.py"
    github_repo_url = "https://github.com/wambaria/HNG_stageone"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/wambaria/HNG_stageone/blob/main/main.py",
        "github_repo_url": "https://github.com/wambaria/HNG_stageone",
        "status_code": 200
    }

    return response_data

if __name__ == "__main__":
    import uvicorn