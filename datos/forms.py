from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
   class Meta:
      model = Usuario
      fields = ('email', 'username', 'password1', 'password2')
