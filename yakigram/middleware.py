from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        print('Get_response=', get_response)
        """Middleware initialization."""
        self.get_response = get_response
        # One-time configuration and initialization / Configuración e inicialización únicas

    def __call__(self, request):
        print('request = ',request)
        # Code to be executed for each request before the view (and later middleware) are called.
        # Código a ejecutar para cada petición antes se llama a la vista (y al middleware posterior).
        
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update_profile'), reverse('logout_view')]:
                        print('me meto aca y que es la verga')
                        return redirect('update_profile')

        response = self.get_response(request)
        #Code to be executed for each request/response after the view is called.
        #Código a ejecutar para cada solicitud/respuesta después  se llama la vista.
        return response
    