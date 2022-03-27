import aiohttp_jinja2
import aiohttp

@aiohttp_jinja2.template('index.html')
async def index(request):
    return