class Post:
    def __init__(self, id, title, subtitle, body) -> None:
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body
    
    @property
    def id(self):
        return self._id
    
    @id.setter 
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def subtitle(self):
        return self._subtitle
    
    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value

    @property
    def body(self):
        return self._body
    
    @body.setter
    def body(self, value):
        self._body = value