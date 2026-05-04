from typing import List, Dict, Any

staff_list = [
    {"id": 1, "name": "Ravi Kumar", "role": "Kitchen Staff", "attendance": "Present", "task": "Prepare Jackfruit Puttu Podi"},
    {"id": 2, "name": "Priya Singh", "role": "Kitchen Staff", "attendance": "Absent", "task": "Millet Porridge Mix Processing"},
    {"id": 3, "name": "Arun Nair", "role": "Inventory Manager", "attendance": "Present", "task": "Check stock levels"},
    {"id": 4, "name": "Meera Menon", "role": "Delivery", "attendance": "Present", "task": "Delivery Route A"},
    {"id": 5, "name": "Rahul Verma", "role": "Delivery", "attendance": "Present", "task": "Delivery Route B"}
]

inventory_list = [
    {"id": 1, "name": "Raw Jackfruit", "quantity": 150, "unit": "kg", "status": "Good"},
    {"id": 2, "name": "Rice Flour", "quantity": 10, "unit": "kg", "status": "Low Stock"},
    {"id": 3, "name": "Drumstick Leaves (Moringa)", "quantity": 5, "unit": "kg", "status": "Low Stock"},
    {"id": 4, "name": "Finger Millet (Ragi)", "quantity": 200, "unit": "kg", "status": "Good"},
    {"id": 5, "name": "Green Bananas", "quantity": 50, "unit": "kg", "status": "Good"},
    {"id": 6, "name": "Barnyard Millet", "quantity": 80, "unit": "kg", "status": "Good"},
    {"id": 7, "name": "Sesame Seeds", "quantity": 2, "unit": "kg", "status": "Low Stock"},
    {"id": 8, "name": "Cumin Seeds", "quantity": 15, "unit": "kg", "status": "Good"},
    {"id": 9, "name": "Coconut Oil", "quantity": 20, "unit": "L", "status": "Good"},
    {"id": 10, "name": "Nannari Roots", "quantity": 8, "unit": "kg", "status": "Warning"}
]

certifications = [
    {"id": 1, "name": "FSSAI License", "expiry_date": "2026-06-15", "status": "Good"},
    {"id": 2, "name": "Health & Hygiene Certificate", "expiry_date": "2026-05-15", "status": "Warning"},
    {"id": 3, "name": "Organic Certification", "expiry_date": "2026-05-08", "status": "Critical"},
]

orders = [
    {"id": "ORD-001", "customer": "Anil D.", "items": ["Jackfruit Puttu Podi", "Coconut Oil"], "status": "Delivered", "total": 450},
    {"id": "ORD-002", "customer": "Sunita K.", "items": ["Sprouted Ragi", "Banana Flour"], "status": "Pending", "total": 600},
    {"id": "ORD-003", "customer": "Vishal T.", "items": ["Millet Health Mix"], "status": "Preparing", "total": 350},
    {"id": "ORD-004", "customer": "Lakshmi R.", "items": ["Nannari Sarbath", "Drumstick Leaf Powder"], "status": "Pending", "total": 550},
    {"id": "ORD-005", "customer": "Kiran V.", "items": ["Banana Stem Kondattam"], "status": "Preparing", "total": 200},
]

deliveries = [
    {"id": "DEL-001", "order_id": "ORD-001", "driver": "Meera Menon", "status": "Completed", "eta": "-"},
    {"id": "DEL-002", "order_id": "ORD-003", "driver": "Rahul Verma", "status": "In Transit", "eta": "15 mins"},
    {"id": "DEL-003", "order_id": "ORD-005", "driver": "Unassigned", "status": "Pending", "eta": "-"},
]

products = [
    {"id": "P1", "name": "Jackfruit Puttu Podi", "description": "Nutritious, low-glycaemic and gluten-free, fibre-rich alternative.", "price": 180, "image": "https://placehold.co/400x300?text=Jackfruit+Puttu"},
    {"id": "P2", "name": "Sprouted Ragi", "description": "Nutrient-dense, gluten-free, and vegan powder.", "price": 250, "image": "https://placehold.co/400x300?text=Sprouted+Ragi"},
    {"id": "P3", "name": "Banana Flour", "description": "Gluten-free, nutrient-dense powder made from dried green bananas.", "price": 200, "image": "https://placehold.co/400x300?text=Banana+Flour"},
    {"id": "P4", "name": "Millet Porridge Mix", "description": "Barnyard millet highly nutritious, fast-cooking.", "price": 150, "image": "https://placehold.co/400x300?text=Millet+Porridge"},
    {"id": "P5", "name": "Drumstick Leaf Powder", "description": "Nutrient-dense, green, herbaceous powder.", "price": 120, "image": "https://placehold.co/400x300?text=Drumstick+Leaf"},
    {"id": "P6", "name": "Naruneendi Sarbath", "description": "Traditional Indian Sarsaparilla cooling drink.", "price": 160, "image": "https://placehold.co/400x300?text=Naruneendi+Sarbath"}
]

dashboard_stats = {
    "total_orders": len(orders),
    "low_stock_alerts": len([i for i in inventory_list if i["status"] in ["Low Stock", "Critical"]]),
    "staff_present": len([s for s in staff_list if s["attendance"] == "Present"]),
    "certifications_expiring": len([c for c in certifications if c["status"] in ["Warning", "Critical"]]),
    "revenue": sum([o["total"] for o in orders if o["status"] != "Cancelled"]),
    "sales_trend": [
        {"name": "Mon", "sales": 4000},
        {"name": "Tue", "sales": 3000},
        {"name": "Wed", "sales": 2000},
        {"name": "Thu", "sales": 2780},
        {"name": "Fri", "sales": 1890},
        {"name": "Sat", "sales": 2390},
        {"name": "Sun", "sales": 3490},
    ],
    "inventory_usage": [
        {"name": "Ragi", "used": 40},
        {"name": "Jackfruit", "used": 30},
        {"name": "Banana", "used": 20},
        {"name": "Millet", "used": 27},
        {"name": "Coconut Oil", "used": 18},
    ]
}
