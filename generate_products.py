import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM products")

products = [
    ("Bone China Plate", "Plates", 350, "https://images.unsplash.com/photo-1583778176476-4a8b02b1c6b9?auto=format&fit=crop&w=400"),
    ("Ceramic Dinner Plate", "Plates", 280, "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?auto=format&fit=crop&w=400"),
    ("Soup Bowl Premium", "Bowls", 220, "https://images.unsplash.com/photo-1604908811913-cca6c6d9c0c5?auto=format&fit=crop&w=400"),
    ("Glass Tumbler Set", "Glassware", 450, "https://images.unsplash.com/photo-1570529765854-2b5c1d1b4b1c?auto=format&fit=crop&w=400"),
    ("Tea Cup Set", "Cups", 300, "https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&w=400"),
    ("Coffee Mug", "Cups", 180, "https://images.unsplash.com/photo-1517685352821-92cf88aee5a5?auto=format&fit=crop&w=400"),
    ("Serving Tray Steel", "Serving", 500, "https://images.unsplash.com/photo-1590080874088-eec64895b423?auto=format&fit=crop&w=400"),
    ("Dinner Set Deluxe", "Dinner Set", 1200, "https://images.unsplash.com/photo-1604909052743-94e838986d24?auto=format&fit=crop&w=400"),
    ("Wine Glass", "Glassware", 400, "https://images.unsplash.com/photo-1514361892635-6fcd9c36b5c4?auto=format&fit=crop&w=400"),
    ("Serving Bowl Large", "Serving", 350, "https://images.unsplash.com/photo-1585238342024-78d387f4a707?auto=format&fit=crop&w=400"),
]

for i in range(30):
    for p in products:
        cursor.execute(
            "INSERT INTO products (name, category, price, image) VALUES (?, ?, ?, ?)",
            (p[0], p[1], p[2] + (i * 10), p[3])
        )

conn.commit()
conn.close()

print("✅ Products with real images added!")