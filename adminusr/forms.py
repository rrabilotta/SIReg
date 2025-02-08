from django.contrib.auth.forms import UserCreationForm

# from registro.models import usuario, usuario_externo, usuario_oficial_externo


class form_CrearUsuarioInterno(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(form_CrearUsuarioInterno, self).__init__(*args, **kwargs)
        
        for fieldname in ["username", "password1", "password2",]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({"class": "form.control"})
