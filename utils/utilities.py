import settings


def height_prct(percentage):
    return (settings.ROOTHEIGHT / 100) * percentage

print(height_prct(25))