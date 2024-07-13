from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse
from dotenv import load_dotenv
import os
from celery.result import AsyncResult
from tasks import send_email_task, log_time_task


app = FastAPI()
load_dotenv()

LOG_FILE_PATH = os.getenv('FILE-PATH')

@app.get("/")
async def handle_requests(sendmail: str = None, talktome: bool = False):
    if sendmail:
        task = send_email_task.delay(sendmail)
        return {"task_id": task.id, "status": "Email sending task queued"}
    elif talktome:
        log_time_task.delay()
        return {"status": "Logging task queued"}
    return {"message": "Provide ?sendmail=email or ?talktome=true in query parameters"}

@app.get("/logs", response_class=PlainTextResponse)
async def get_logs():
    if not os.path.exists(LOG_FILE_PATH):
        raise HTTPException(status_code=404, detail="Log file not found")
    
    with open(LOG_FILE_PATH, "r") as log_file:
        logs = log_file.read()
        # return f"<pre>{log_content}</pre>"

    return logs

if __name__ == '__main__':
    app.run(debug=True)