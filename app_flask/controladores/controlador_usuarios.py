from flask import render_template,  redirect, request, flash
from app_flask.modelos.modelo_usuario import Usuario
from app_flask import app


@app.route('/')
def desplegar_form():
    return render_template('/amistades.html')

@app.route('/agregar/usuario', methods=['POST'])
def agregar_usuario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    
    # Validar los datos, por ejemplo, asegurarse de que no estén vacíos
    
    if not nombre or not apellido:
        flash('Por favor, ingrese nombre y apellido.', 'error')
        return redirect('/')  # Redirigir a la página principal o a donde sea necesario
    
    # Crear un diccionario con los datos para el usuario
    datos_usuario = {
        'nombre': nombre,
        'apellido': apellido
    }
    
    # Llamar al método para crear un usuario en tu modelo
    Usuario.agregar_usuario(datos_usuario)
    
    flash('Usuario agregado correctamente.', 'success')
    return redirect('/')  # Redirigir a la página principal o a donde sea necesario

@app.route('/crear/amistad', methods=['POST'])
def crear_amistad():
    usuario_id = request.form['usuario_id']
    amigo_id = request.form['amigo_id']
    
    # Validar los datos, asegurarse de que los IDs no estén vacíos, por ejemplo
    
    if not usuario_id or not amigo_id:
        flash('Por favor, seleccione un usuario y un amigo.', 'error')
        return redirect('/')  # Redirigir a la página principal o a donde sea necesario
    
    # Llamar al método para crear una amistad en tu modelo de usuario
    Usuario.crear_amistad(usuario_id, amigo_id)
    
    flash('Amistad creada correctamente.', 'success')
    return redirect('/')  # Redirigir a la página principal o a donde sea necesario
