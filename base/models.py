from django.db.models import Model, DateTimeField, BooleanField

class BaseModel(Model):

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
   
    is_deleted = BooleanField(default=False)
   
    class Meta:
        abstract = True
    
    def delete(self):
        self.is_deleted = True
        self.save()
        
    def restore(self):
        self.is_deleted = False
        self.save()