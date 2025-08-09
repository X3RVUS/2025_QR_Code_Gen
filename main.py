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
