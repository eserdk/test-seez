class BaseModel:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    @classmethod
    def from_dict(cls, adict):
        return cls(**adict)

    def to_dict(self):
        return vars(self)
