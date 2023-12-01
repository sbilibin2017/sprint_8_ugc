import logging

import libs.app as app_module
import uvicorn

logger = logging.getLogger(__name__)

app_instance = app_module.Application()
app = app_instance.create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
