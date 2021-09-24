import threading

class LockGroup(object):
    lock_dict = {}
    lock = threading.Lock()

    # Returns a lock object, unique for each unique value of param.
    # The first call with a given value of param creates a new lock, subsequent
    # calls return the same lock.
    @staticmethod
    def get_lock(param):
        with LockGroup.lock:
            if param not in LockGroup.lock_dict:
                LockGroup.lock_dict[param] = threading.Lock()
            return LockGroup.lock_dict[param]