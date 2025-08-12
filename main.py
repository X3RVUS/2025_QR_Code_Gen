import qrcode

# ==== Konfiguration ====
url = ""  # Deine URL hier eintragen
output_file = "qrcode.png"       # Name der Ausgabedatei

# === QR-Code erzeugen ===
qr = qrcode.QRCode(
    version=1,  # Größe des QR-Codes (1 = kleinste)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # hohe Fehlerkorrektur
    box_size=10,  # Größe der einzelnen Kästchen
    border=4      # Rahmenbreite
)
qr.add_data(url)
qr.make(fit=True)

# === QR-Code als Bild speichern ===
img = qr.make_image(fill_color="black", back_color="white")
img.save(output_file)

print(f"QR-Code gespeichert unter: {output_file}")
print("Du kannst den QR-Code scannen, um die URL zu öffnen.")
# Hinweis: Stelle sicher, dass die Bibliothek 'qrcode' installiert ist.
# Installiere sie mit: pip install qrcode[pil]
# Hinweis: Stelle sicher, dass die URL korrekt ist.
# Hinweis: Der QR-Code kann mit jedem QR-Code-Scanner gelesen werden.