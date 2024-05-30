from PIL import Image

class DeploymentCard:
    def __init__(self, name):
        self.name = name
        self.image = None

    def loadDeploymentImage(self, filepath):
        """Load the battlefield deployment image"""
        try:
            self.image = Image.open(filepath)
            print(f"Image loaded from {filepath}")
        except Exception as e:
            print(f"Error loading image: {e}")

    def saveDeploymentImage(self, filepath):
        """Save the battlefield to filepath"""
        if self.image:
            try:
                self.image.save(filepath)
                print(f"Image saved to {filepath}")
            except Exception as e:
                print(f"Error saving image: {e}")
        else:
            print("No image to save")

    def getDeployment(self):
        return self.image