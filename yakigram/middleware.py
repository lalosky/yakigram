from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response
        # One-time configuration and initialization / Configuración e inicialización únicas

    def __call__(self, request):

        # Code to be executed for each request before the view (and later middleware) are called.
        # Código a ejecutar para cada petición antes se llama a la vista (y al middleware posterior).
        # recuerda toda peticion va a pasar por aca
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    print('request.path',request.path)
                    print('reverse("update_profile")',reverse('update_profile'))
                    print("reverse('logout_view')",reverse('logout_view'))
                    if request.path not in [reverse('update_profile'), reverse('logout_view')]:
                        print('me meto aca y que es la verga')
                        return redirect('update_profile')
        print('REQUEST')
        response = self.get_response(request)
        print('RESPONSE')
        #Code to be executed for each request/response after the view is called.
        #Código a ejecutar para cada solicitud/respuesta después  se llama la vista.
        return response
    