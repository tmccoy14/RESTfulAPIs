from pyramid.config import Configurator
from cornice import Service

# Create a Service object
QUOTES = Service(name='quotes',
                 path='/',
                 description='Get quotes')

# GET method for QUOTES
@QUOTES.get()
def get_quote(request):
    return {
        'William Shakespeare': {
            'quote': ['Love all, trust a few, do wrong to none',
            'Some are born great, some achieve greatness, and some have greatness thrust upon them.']
    },
    'Linus': {
        'quote': ['Talk is cheap. Show me the code.']
        }
    }

# Use Scan to find all decorated functions and add them to the configuration
with Configurator() as config:
    config.include("cornice")
    config.scan()
    application = config.make_wsgi_app()

# Run the service -- python -m twisted web --wsgi=main.application
# Navigate to localhost -- http://localhost:8080