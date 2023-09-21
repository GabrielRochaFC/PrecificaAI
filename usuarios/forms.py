from django import forms

class LoginForms(forms.Form):
  nome_login = forms.CharField(
    label="Nome de Usuário",
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "class" : "form-control",
        "placeholder" : "Ex.: JoãoSilva123"
      }
    )
  )
  senha = forms.CharField(
    label="Senha",
    max_length=70,
    required=True,
    widget=forms.PasswordInput(
      attrs={
        "class" : "form-control",
        "placeholder" : "Digite sua senha"
      }
    )
  )

class CadastroForms(forms.Form):
  primeiro_nome = forms.CharField(
    label="Primeiro nome",
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "class" : "form-control",
        "placeholder" : "Ex.: João"
      }
    )
  )
  sobrenome = forms.CharField(
    label="Sobrenome",
    required=True,
    max_length=100,
    widget=forms.TextInput(
      attrs={
        "class" : "form-control",
        "placeholder" : "Ex.: Silva"
      }
    )
  )
  nome_cadastro = forms.CharField(
    label="Nome de Usuário",
    required=True,
    max_length=250,
    widget=forms.TextInput(
      attrs={
        "class" : "form-control",
        "placeholder" : "Ex.: JoãoSilva123"
      }
    )
  )
  email = forms.EmailField(
    label="Email",
    required=True,
    max_length=100,
    widget=forms.EmailInput(
      attrs={
        "class" : "form-control",
        "placeholder" : "Ex.: joaosilva@xpto.com"
      }
    )
  )
  senha_1 = forms.CharField(
    label="Senha",
    max_length=70,
    required=True,
    widget=forms.PasswordInput(
      attrs={
        "class" : "form-control",
        "placeholder" : "Digite sua senha"
      }
    )
  )
  senha_2 = forms.CharField(
    label="Confirme sua senha",
    max_length=70,
    required=True,
    widget=forms.PasswordInput(
      attrs={
        "class" : "form-control",
        "placeholder" : "Digite sua senha novamente"
      }
    )
  )

  def clean_nome_cadastro(self):
    nome = self.cleaned_data.get("nome_cadastro")

    if nome:
      nome = nome.strip()
      if ' ' in nome:
        raise forms.ValidationError("Espaços não são permitidos neste campo.")
      else:
        return nome
  
  def clean_senha_2(self):
    senha_1 = self.cleaned_data.get("senha_1")
    senha_2 = self.cleaned_data.get("senha_2")

    if senha_1 != senha_2:
      raise forms.ValidationError("As senhas não são iguais.")