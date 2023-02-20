from fastapi import APIRouter

from dbs_assignment.endpoints import hello,version

router = APIRouter()
router.include_router(hello.router, tags=["hello"])
router.include_router(version.router, tags=["version"])

