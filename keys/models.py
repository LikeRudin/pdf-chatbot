
from django.db.models import CASCADE, CharField, BooleanField, ForeignKey
from base.models import BaseModel
from users.models import User

KEY_KINDS = [
    ('open_ai', 'OpenAI'),
    ('claude', 'Claude'),
]

class Key(BaseModel):
    uesr = ForeignKey(User, on_delete=CASCADE, related_name="keys")
    name = CharField(help_text="api key name by user", max_length=100, blank=False, null=False)
    is_valid = BooleanField(default=False)
    is_selected = BooleanField(default=False)
    key_kind = CharField(max_length=20, choices=KEY_KINDS)
    encrypted_key = CharField(max_length=255, blank=False)
    
    def save(self, *args, **kwargs):
        if self.is_selected:
            Key.objects.filter(user=self.user, is_selected=True).update(is_selected=False)
        super().save(*args, **kwargs)