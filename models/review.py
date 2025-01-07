from models.base_model import BaseModel

#!/usr/bin/python3
""" Review module for the HBNB project """

class Review(BaseModel):
    """ Review class to store review information """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initializes Review instance """
        super().__init__(*args, **kwargs)
        if 'place_id' in kwargs:
            self.place_id = kwargs['place_id']
            if not isinstance(self.place_id, str):
                raise TypeError("place_id must be a string")
            if not self.place_id:
                raise ValueError("place_id cannot be empty")
        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']
            if not isinstance(self.user_id, str):
                raise TypeError("user_id must be a string")
            if not self.user_id:
                raise ValueError("user_id cannot be empty")
            if not self.get_or_create(BaseModel, id=self.user_id):
                raise ValueError("user_id must be a valid User.id")
        if 'text' in kwargs:
            self.text = kwargs['text']
            if not isinstance(self.text, str):
                raise TypeError("text must be a string")
            if not self.text:
                raise ValueError("text cannot be empty")
        if 'id' in kwargs:
            self.id = kwargs['id']
            if not isinstance(self.id, str):
                raise TypeError("id must be a string")
            if not self.id:
                raise ValueError("id cannot be empty")
        self.save()
        self.updated_at = self.get_updated_at()
        self.created_at = self.get_created_at()
        self.id = self.update_id()
        self.place_id = self.place_id

    def update_id(self):
        """ Updates the id with a unique UUID """
        import uuid
        self.id = str(uuid.uuid4())
        return self.id
    
    def get_updated_at(self):
        """ Returns the updated_at attribute """
        return self.updated_at
    
    def get_created_at(self):
        """ Returns the created_at attribute """
        return self.created_at
    

revvew = Review()
