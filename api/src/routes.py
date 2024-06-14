import logging
from fastapi import APIRouter, Request, Response, status
from repository import BlogRepository, Post

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/")
async def health_check():
    return {"status": "ok"}


@router.post("/blog")
async def create_blog_post(request: Request, response: Response):
    try:
        data = await request.json()
        post = Post(data["title"], data["content"])
        BlogRepository.add(post)

        response.status_code = status.HTTP_201_CREATED
        return {"status": "success", "id": post.id}
    except Exception as e:
        logger.error("Error creating blog post: %s on create", str(e))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}


@router.get("/blog")
async def get_blog_posts(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"posts": [post.to_json() for post in BlogRepository.get_all()]}


@router.get("/blog/{id}")
async def get_blog_post(id: int, response: Response):
    post = BlogRepository.get_by_id(id)
    if post:
        response.status_code = status.HTTP_200_OK
        return post.to_json()

    logger.warning("Blog post with ID %s not found for retrieval", id)
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "Post not found"}


@router.delete("/blog/{id}")
async def delete_blog_post(id: int, response: Response):
    if BlogRepository.delete(id):
        response.status_code = status.HTTP_200_OK
        return {"status": "success"}

    logger.warning("Blog post with ID %s not found for deletion", id)
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error": "Post not found"}


@router.put("/blog/{id}")
async def update_blog_post(id: int, data: dict, response: Response):
    try:
        if BlogRepository.update(id, data):
            response.status_code = status.HTTP_200_OK
            return {"status": "success"}

        logger.warning("Blog post with ID %s not found for updating", id)
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Post not found"}

    except Exception as e:
        logger.error("Error updating blog post: %s", str(e))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
