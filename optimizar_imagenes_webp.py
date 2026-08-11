import os
import sys
from PIL import Image

def optimize_images():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    uploaded_dir = r"C:\Users\Pelon\.gemini\antigravity\brain\30c77d14-0db0-471f-a890-f1604fbb8aff\.user_uploaded"
    
    # 1. Optimizar logotipo a logo.webp conservando transparencia
    logo_src = os.path.join(base_dir, "logo.png")
    if not os.path.exists(logo_src):
        logo_src = os.path.join(uploaded_dir, "media_1785952970048.png")
    
    logo_out = os.path.join(base_dir, "logo.webp")
    
    print(f"Procesando logotipo desde: {logo_src}")
    with Image.open(logo_src) as img_logo:
        # Asegurar modo RGBA para preservar transparencia
        if img_logo.mode != 'RGBA':
            img_logo = img_logo.convert('RGBA')
        img_logo.save(logo_out, 'WEBP', lossless=True, quality=100)
        print(f"Logotipo guardado exitosamente: {logo_out} (Tamaño: {os.path.getsize(logo_out)} bytes)")

    # 2. Optimizar foto del Hero a hero_nectar.webp con compresión optimizada y sin metadatos
    hero_src = os.path.join(uploaded_dir, "media_1786408769040.jpg")
    hero_out = os.path.join(base_dir, "hero_nectar.webp")
    
    print(f"Procesando foto del Hero desde: {hero_src}")
    with Image.open(hero_src) as img_hero:
        # Convertir a RGB si es necesario
        if img_hero.mode in ('RGBA', 'LA', 'P'):
            img_hero = img_hero.convert('RGB')
        # Guardar como WebP optimizado con calidad balanceada y eliminando EXIF/metadatos
        img_hero.save(hero_out, 'WEBP', quality=82, method=6, keep_metadata=False)
        print(f"Hero guardado exitosamente: {hero_out} (Tamaño: {os.path.getsize(hero_out)} bytes)")

    # También guardar una copia en logos/logo.webp si la carpeta existe
    logos_dir = os.path.join(base_dir, "logos")
    if os.path.exists(logos_dir):
        with Image.open(logo_src) as img_logo:
            if img_logo.mode != 'RGBA':
                img_logo = img_logo.convert('RGBA')
            img_logo.save(os.path.join(logos_dir, "logo.webp"), 'WEBP', lossless=True, quality=100)

if __name__ == '__main__':
    optimize_images()
