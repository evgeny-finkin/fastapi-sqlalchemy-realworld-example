import uvicorn
from fastapi import FastAPI

from router import router

app = FastAPI(
    title='Real world app (RWA) backend using fastAPI, poetry and sqlalchemy',
    description='A backend for RWA using specs as defined in https://realworld-docs.netlify.app/docs/specs/backend-specs/introduction',
    license_info={
        'name': 'MIT License'
    }
)

app.include_router(router)
# users.Base.create_all(bind=postgres.engine)

# if __name__ == '__main__':
#     uvicorn.run(
#         'main:app',
#         host='0.0.0.0',
#         reload=True,
#         port=8000
#     )

# 2:36:23
