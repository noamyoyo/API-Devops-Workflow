from fastapi import APIRouter
from fastapi import Request
import time
import datetime

router = APIRouter()

@router.get("/api/") # get current date with no parameters, returns utc date and unix timestamp
async def check_date_no_params():
    unix_now = int(time.time()*1000.0)
    utc_now = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    return {"unix": unix_now, "utc": utc_now}

@router.get("/api/{date}") # get date of right format: YYYY-MM-DD or unix timestamp, returns utc date and unix timestamp
async def check_date(date):
    date_valid = is_date_valid(date)
    if date_valid:
        return {"unix": date_valid, "utc": unix_to_utc_timestamp(date_valid)}
    unix_valid = is_unix_valid(date)
    if unix_valid:
        return {"unix": int(date), "utc": unix_valid}
    else:
        return {"error" : "Invalid Date"}

def unix_to_utc_timestamp(unix):
    utc_timestamp = datetime.datetime.fromtimestamp(int(unix)/1000)
    utc_timestamp = datetime.datetime.strftime(utc_timestamp, "%a, %d %b %Y %H:%M:%S GMT")
    return utc_timestamp

def date_to_unix(date):
    date_obj = datetime.datetime.strptime(date,"%Y-%m-%d")
    unix_timestamp = date_obj.timestamp() * 1000
    return int(unix_timestamp)

def is_date_valid(date):
    correctDate = False
    try:
        unix = date_to_unix(date)
        correctDate = True
        return unix
    except ValueError:
        correctDate = False
    return correctDate

def is_unix_valid(unix):
    correctDate = False
    try:
        utc = unix_to_utc_timestamp(unix)
        correctDate = True
        return utc
    except ValueError:
        correctDate = False
    return correctDate



