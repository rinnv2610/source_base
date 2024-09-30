from rest_framework.renderers import JSONRenderer


class ApiRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        response = data

        if str(status_code).startswith('2'):
            results = data.pop('results', None) if data and 'results' in data else None
            response = {
                "meta": data if results else {},
                "data": results if results else data
            }
        return super(ApiRenderer, self).render(response, accepted_media_type, renderer_context)
