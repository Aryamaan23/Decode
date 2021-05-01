from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.compile import router as CodeCompileRouter
from .routes.convertPseudo import router as ConvertCodeIntoPseudoRouter
from .routes.translatePseudo import router as TranslateRouter
from .routes.warnings import router as WarningsRouter
from .routes.shareCode import router as ShareCodeRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(CodeCompileRouter, tags=["Code Compile"], prefix="/api/v1/compile")
app.include_router(ConvertCodeIntoPseudoRouter, tags=["Convert Code into Pseudo Code"], prefix="/api/v1/convert")
app.include_router(TranslateRouter, tags=["Translate Pseudo Code"], prefix="/api/v1/translate")
app.include_router(WarningsRouter, tags=["Warnings"], prefix="/api/v1/warnings")
app.include_router(ShareCodeRouter, tags=["Share Code"], prefix="/api/v1/share")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Decode"}
