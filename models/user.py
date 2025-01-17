'''module importation'''
from models.base_model2 import BaseModel
#!/usr/bin/python3
"""
User Module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def create(self):
        """Creates a new user instance"""
        # Replace save_to_db with actual save logic
        self.save()

    def save(self):
        """Saves the user instance"""
        super().save()  # Ensure BaseModel's save logic is used
