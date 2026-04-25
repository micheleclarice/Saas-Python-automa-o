from starlette.middleware.base import BaseHTTPMiddleware
from app.tenant import get_tenant


class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.tenant = get_tenant(request)
        return await call_next(request)