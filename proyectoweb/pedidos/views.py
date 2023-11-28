from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from pedidos.models import LineaPedido, Pedido
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from tienda.models import Producto



# Create your views here.
@login_required
def realizar_pedido(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    if request.method == 'POST':
        cantidad_pedido = int(request.POST.get('cantidad', 0))

        if 0 < cantidad_pedido <= producto.cantidad_disponible:
            # Crear un nuevo pedido si no existe uno activo para el usuario
            pedido, created = Pedido.objects.get_or_create(user=request.user)

            # Crear un nuevo detalle del pedido
            detalle_pedido = LineaPedido(user=request.user, producto=producto, pedido=pedido, cantidad=cantidad_pedido)
            detalle_pedido.save()

            # Actualizar la cantidad disponible del producto
            producto.cantidad_disponible -= cantidad_pedido
            producto.save()

            # Resto de la lógica del pedido...

    return render(request, '', {'producto': producto})








@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
            
            
        ))
        
    LineaPedido.objects.bulk_create(lineas_pedido)
    
    enviar_mail(
            pedido=pedido,
            lineas_pedido=lineas_pedido,
            nombreusuario=request.user.username,
            emailusuario=request.user.email
    )
    
    messages.success(request, "El pedido se creo correctamente")
    
    return redirect("../tienda")
    
def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html", {
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario"),
        
        
        
        
    })
    
    mensaje_texto=strip_tags(mensaje)
    from_email="corralonlapabloneta@gil.com"
    to=kwargs.get("emailusuario")
    #to="joseagustinfigueroa8@gmail.com"
    
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)