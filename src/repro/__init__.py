import pathlib

from fastapi.templating import Jinja2Templates
from starlette.requests import Request

templates = Jinja2Templates(directory=pathlib.Path(__file__).parent / "templates")
_ = templates.TemplateResponse(
    request=Request(scope={"type": "http"}),  # Mock sccope
    name="greet.html",
    context={"name": "Tom"},
)
