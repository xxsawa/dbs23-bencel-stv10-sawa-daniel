from fastapi import APIRouter


import psycopg2

router = APIRouter()

@router.get("/v1/status")
async def version():
    
    db_version = "Connection error"
    try:
        conn = psycopg2.connect("dbname=dbs user=postgres password=password host=172.17.0.2 port=5432")
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
    except:
        print("Cannot connect to database")

    return {
        'version': db_version
    }
