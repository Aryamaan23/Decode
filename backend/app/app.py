from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Decode"}
