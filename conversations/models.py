from django.db.models import ForeignKey, CharField, TextField, SET_NULL, CASCADE, IntegerField

from base.models import BaseModel

from users.models import User

class Conversation(BaseModel):
    title = CharField(help_text="Private ChatRoom Title", max_length=100, blank=False, null=False)
    user = ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.title:
            if not self.pk:
                super().save(*args, **kwargs)
            self.title = f"ChatRoom: {self.created_at.strftime('%y-%m-%d-%H-%M')}"
        super().save(*args, **kwargs)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

ROLE_CHOICES = [
    ('user', 'User'),
    ('system', 'System'),
    ('chatbot', 'Chatbot'),
]
class Message(BaseModel):
    role = CharField(choices=ROLE_CHOICES, default="system")
    payload = TextField(blank=False)
    token_number = IntegerField(default=0)
    
    user = ForeignKey(User, related_name="messages", on_delete=SET_NULL, null=True)
    conversation = ForeignKey(Conversation, related_name="messages", on_delete=CASCADE)

    

    