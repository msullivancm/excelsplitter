from api_brasil import APIBrasilClient, WhatsAppApi

# Instancie o client da APIBrasil
api_brasil_client = APIBrasilClient(bearer_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwcC5hcGlicmFzaWwuaW8vYXV0aC9jYWxsYmFjayIsImlhdCI6MTc1MDY4MjUwNiwiZXhwIjoxNzgyMjE4NTA2LCJuYmYiOjE3NTA2ODI1MDYsImp0aSI6IktJc2JxekRUTHNYeG1SQUUiLCJzdWIiOiI5OTE2IiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.jQd6ivrIUYRagxeDCYW6DLsy2Gd_xJrPDRC0WergOy8")
# Você pode encontrar o seu bearer token em https://apibrasil.com.br na área de Credenciais


## Usando a API de WhatsApp
whatsapp_api = WhatsAppApi(api_brasil_client=api_brasil_client, device_token="4230c458-70ca-4758-b115-f2659d66df0d") 
### Você pode encontrar o seu device token em https://apibrasil.com.br na área de Dispositivos


# # Enviando uma mensagem
whatsapp_api.to_number(phone_number="5521998949878")   # Número de telefone para enviar a mensagem
response, status_code = whatsapp_api.send_message(message="Hello, estou integrado com sucesso com Api Brasil!")

print(response, status_code)


# # Enviando um arquivo para o número definido no método to_number
response, status_code = whatsapp_api.send_file(file_path="https://apibrasil.io/img/capa.png", file_description="Bem vindo a API Brasil")

print(response, status_code)