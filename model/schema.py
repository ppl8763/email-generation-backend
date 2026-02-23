from pydantic import BaseModel


class new(BaseModel):
    title:str
    about:str

class email(BaseModel):
    purpose:str
    recipient_type:str
    tone:str
    message:str
    sender_name:str
    
   