import os
import sys
import logging
import uvicorn


logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)-8s[%(name)s] %(asctime)s: %(message)s")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.debug('start')

#
# Start server
#
uvicorn.run("api.api.root:app", host='0.0.0.0', port=8080, reload=True)
