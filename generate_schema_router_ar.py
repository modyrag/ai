# generate_schema_router_ar.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils import generate_text, search_image

router = APIRouter(prefix="/ar")

# Define a Pydantic model for the request body
class UserText(BaseModel):
    user_text: str

# Define a function to handle the POST request at `/generate-schema`
@router.post("/generate-schema", response_model=dict)
def generate_schema_route(input: UserText):
    """
    Generate a schema for a hero section of a website based on user input text.
    """
    user_text = input.user_text
    if not user_text:
        raise HTTPException(status_code=400, detail="user_text is required")

    # Generate text for different sections of the website
    title = generate_text(f"اقترح اسمًا لموقع ويب عن {user_text}")
    description = generate_text(f"أنشئ وصفًا موجزًا لموقع ويب عن {user_text}")

    # Define the schema for the hero section
    schema = {
        "hero": {
            "title": title,
            "description": description,
            "buttonText": "ابدأ الآن",
            "icon": "https://res.cloudinary.com/duc04fwdb/image/upload/v1701813389/templates/template_one/Vector_5_vvvt2o.svg",
            "imgUrl": search_image(f"أحتاج صورة لاستخدامها كخلفية لموقع ويب عن {user_text}"),
        },
    }

    return schema
