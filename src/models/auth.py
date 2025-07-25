from pydantic import BaseModel, Field


class AuthLoginRequest(BaseModel):
    """Request model for user login"""
    email: str = Field(description="User's email address")
    password: str = Field(description="User's password")


class AuthLoginResponse(BaseModel):
    """Response model for successful user login"""
    id: str = Field(description="ID of the authenticated user")
    access_token: str = Field(description="Access token for authentication.")


