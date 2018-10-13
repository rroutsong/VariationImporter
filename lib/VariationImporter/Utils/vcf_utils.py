

class InvalidVCFException(Exception):
    """
        Custom exception class for VCF files
    """
    def __init__(self, file_path, message):
        self.file_path = file_path
        self.message = message

    def __str__(self):
        return repr(self.message + self.file_path)