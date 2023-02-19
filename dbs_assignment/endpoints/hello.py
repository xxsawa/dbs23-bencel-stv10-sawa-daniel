from fastapi import APIRouter

from dbs_assignment.config import settings

import psycopg2

router = APIRouter()

conn = psycopg2.connect("dbname=dbs user=xsawa password=SuperTajneHeslo host=127.0.0.1 port=5432")
cur = conn.cursor()
cur.execute('SELECT version()')
db_version = cur.fetchone()
cur.close()
conn.close()


@router.get("/v1/hello")
async def hello():
    return {
        'hello': settings.NAME
    }

@router.get("/v1/status")
async def version():
    return {
        'version': db_version
    }
