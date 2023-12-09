from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the application
storage = FileStorage()
# Call reload() method on this variable to load existing objects from the file
storage.reload()
