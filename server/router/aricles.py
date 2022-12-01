from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, List

from services import postgres, api, jwt
from schemas import Article, UpdatedArticle, Comment
router = APIRouter()


@router.get('/{tag}{author}{favorited}', response_model=List[Article])
async def list_of_articles(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None,
    limit: int = 20,
    offset: int = 0,
    tag: str = Path(...),
    author: str = Path(...),
    favorited: str = Path(...),
):
    # obj = await jwt.decode(token)
    articles = await api.articles.get_articles_by_tegs(session, limit, offset, tag, author, favorited)
    return articles


@router.get('/feed', response_model=List[Article])
async def feed(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None,
    limit: int = 20,
    offset: int = 0
):
    # obj = await jwt.decode(token)
    articles = await api.articles.get_articles_by_feed(session, limit, offset)
    return articles


@router.get('/{slug}', response_model=Article)
async def get_article(
    session: AsyncSession = Depends(postgres.get_async_session),
    slug: str = Path(...)
):
    # obj = await jwt.decode(token)
    articles = await api.articles.get_article(session, slug)
    return articles


@router.post('/')
async def create_article(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None,
    article: Article = None
):
    # obj = await jwt.decode(token)
    await api.articles.create_article(session, article)
    return None


@router.put('/{slug}')
async def update_article(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None,
    slug: str = Path(...),
    updated_article: UpdatedArticle = None
):
    # obj = await jwt.decode(token)
    await api.articles.update_article(session, slug, updated_article)
    return None


@router.put('/{slug}')
async def delete_article(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None,
    slug: str = Path(...),
):
    # obj = await jwt.decode(token)
    await api.articles.delete_article(session, slug)
    return None


@router.post('/{slug}/comments')
async def add_comment(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None,
    slug: str = Path(...),
    comment: Comment = None
):
    # obj = await jwt.decode(token)
    await api.comments.add_comment(session, slug, comment)
    return None


@router.post('/{slug}/comments')
async def get_comments(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None,
    slug: str = Path(...),
    comment: Comment = None
):
    # obj = await jwt.decode(token)
    await api.comments.get_comments(session, slug, comment)
    return None


@router.delete('/{slug}/comments/{id}')
async def delete_comment(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None,
    slug: str = Path(...),
    id: str = Path(...),
):
    # obj = await jwt.decode(token)
    await api.comments.delete_comment(session, slug, id)
    return None


@router.post('/{slug}/comments/favorite')
async def favorite_article(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None,
    slug: str = Path(...),
):
    # obj = await jwt.decode(token)
    await api.comments.favorite_article(session, slug)
    return None


@router.delete('/{slug}/comments/favorite')
async def unfavorite_article(
    session: AsyncSession = Depends(postgres.get_async_session),
    token: str = None,
    slug: str = Path(...),
):
    # obj = await jwt.decode(token)
    await api.comments.unfavorite_article(session, slug)
    return None
