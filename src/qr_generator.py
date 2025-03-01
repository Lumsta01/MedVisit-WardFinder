import qrcode

def generate_qr(visitor_id):
    qr = qrcode.make(f"https://medvisit.com/verify/{visitor_id}")
    qr.save(f"qr_{visitor_id}.png")
    
    print(f"QR Code generated: qr_{visitor_id}.png")
    
generate_qr(1234)

