# basiclogger
A simple python logger that I created.

### Usage
```py
import basiclogger
logger = basiclogger.Logger(debug=True) # incase you want to print out debug statements.

logger.warn("This is a warning")
logger.fail("This is an error")
logger.success("This is a success")
logger.debug("This will only print if debug = True")
```
