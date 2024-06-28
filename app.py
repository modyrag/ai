from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from generate_schema_router_en import router as generate_schema_router_en
from generate_schema_router_ar import router as generate_schema_router_ar

# Create a new FastAPI app instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Define a root path to verify the server is running
@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")

# Include the routers
app.include_router(generate_schema_router_en, prefix="/en")
app.include_router(generate_schema_router_ar, prefix="/ar")
