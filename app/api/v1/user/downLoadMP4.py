from fastapi import APIRouter, HTTPException
from bs4 import BeautifulSoup
import requests

router = APIRouter()


@router.get("/get_video_src")
def get_video_src(url: str):
    print(url)
    try:
        # 使用 requests 库从提供的 URL 下载页面内容
        response = requests.get(url)

        # 检查响应状态码，确保请求成功
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code, detail="Failed to fetch the URL."
            )

        # 解析 HTML 内容
        soup = BeautifulSoup(response.text, "html.parser")

        # 查找第一个 video 标签的 src 属性
        video_tag = soup.find("video")
        if video_tag and video_tag.get("src"):
            return {"video_src": video_tag["src"]}
        else:
            raise HTTPException(
                status_code=404, detail="No video src found in the page."
            )

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail="Error while fetching the URL.")
