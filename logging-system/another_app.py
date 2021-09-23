from loging import Loging
log = Loging.getInstance()
def function2():
    log.error("this is another error msg")
    log.info("this is another info msg")
    log.debug("this is another debug msg")

