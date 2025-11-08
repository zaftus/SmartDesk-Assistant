import os
from .logging_config import logger

class Automation:
    @staticmethod
    def organize_folder(path):
        if not os.path.exists(path):
            logger.warning(f"Folder {path} does not exist!")
            return

        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                ext = file.split('.')[-1]
                folder = os.path.join(path, ext)
                os.makedirs(folder, exist_ok=True)
                os.rename(file_path, os.path.join(folder, file))
        logger.info(f"Folder {path} organized by file type.")
