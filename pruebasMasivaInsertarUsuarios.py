import requests

url = "http://4.246.181.91:8080/Auth/Register"

usuarios = []
for i in range(1, 101):
    usuario = {
        "Nombre": f"Usuario{i}",
        "Correo": f"usuario{i}@ejemplo.com",
        "Clave": f"Password{i:03d}!",
        "ConfirmarClave": f"Password{i:03d}!"
    }
    usuarios.append(usuario)

for usuario in usuarios:
    response = requests.post(url, data=usuario, allow_redirects=False)
    print(f"Usuario: {usuario['Correo']} - Status: {response.status_code}")
    if response.status_code in (302, 200):
        print("Usuario registrado correctamente (redirección o éxito detectado).")
    else:
        print("Respuesta:", response.text)
