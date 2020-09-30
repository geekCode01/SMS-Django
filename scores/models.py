from django.db import models
from twilio.rest import Client
# Create your models here.

class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = 'AC3ccdc3e0373444a8f7486162d73873be'
            auth_token = '2ca5d80488fa6e391f66aebfaa671bf4'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'The current result is bad - {self.result}',
                                        from_='+12058317484',
                                        to='+919877507178'
                                    )

            print(message.sid)
        return super().save(*args,**kwargs)