import fastapi
import fastapi.openapi.docs
import fastapi.openapi.utils

import controllers.names
import controllers.users


app = fastapi.FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

app.include_router(controllers.users.router)
app.include_router(controllers.names.router)


@app.get("/docs")
async def docs():
    return fastapi.openapi.docs.get_swagger_ui_html(openapi_url="openapi.json", title="docs")


@app.get("/openapi.json")
async def openapi():
    return fastapi.openapi.utils.get_openapi(title="FastAPI", version="0.1.0", routes=app.routes)
