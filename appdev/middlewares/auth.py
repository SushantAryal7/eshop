from django.shortcuts import redirect, render


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        returnurl = request.META['PATH_INFO']

        if not request.session.get('customer'):
            return redirect(f'login?returnurl={returnurl}')

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware