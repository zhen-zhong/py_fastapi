from fastapi import APIRouter
import requests
# from app.schemas.user import UserRegister

router = APIRouter()


@router.post("/register")
def register():
    url = "https://k301o.cloudatacdn.com/u5kj7fdbrtblsdgge4e4ooidiqykdyci2cprs7edvpsmfns5szato3hy52uq/ht1bd2lgrk~ruN06NuJog?token=qrgk8v8do0vnm26hg7cowfhx&expiry=1746764082189"

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "identity;q=1, *;q=0",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,id;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Range": "bytes=0-",
        "Referer": "https://do7go.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    response = requests.get(url, headers=headers, stream=True)

    if response.status_code == 206:
        with open("video.mp4", "wb") as video_file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    video_file.write(chunk)
        video_message = "Video downloaded and saved as video.mp4"
    else:
        video_message = f"Failed to download video, status code: {response.status_code}"

    return {
        "video_status": video_message,
    }
