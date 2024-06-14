from typing import List


class Post:
    ID: int = 0

    def __init__(self, title, content):
        Post.ID += 1
        self.id = Post.ID
        self.title = title
        self.content = content

    def __str__(self) -> str:
        return f"{self.id} - {self.title} - {self.content}"

    def __repr__(self) -> str:
        return f'Post({self.id}, "{self.title}", "{self.content}")'

    def to_json(self) -> dict:
        return {"id": self.id, "title": self.title, "content": self.content}


class BlogRepository:
    POSTS: List[Post] = []

    @staticmethod
    def get_all() -> List[Post]:
        return BlogRepository.POSTS

    @staticmethod
    def get_by_id(id: int) -> Post:
        for post in BlogRepository.POSTS:
            if post.id == id:
                return post

        return None

    @staticmethod
    def add(post: Post) -> None:
        BlogRepository.POSTS.append(post)

    @staticmethod
    def delete(id: int) -> bool:
        for post in BlogRepository.POSTS:
            if post.id == id:
                BlogRepository.POSTS = [
                    post for post in BlogRepository.POSTS if post.id != id
                ]
                return True

        return False

    @staticmethod
    def update(id, data) -> bool:
        for post in BlogRepository.POSTS:
            if post.id == id:
                post.title = data["title"]
                post.content = data["content"]
                return True

        return False
