from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mock_data

app = FastAPI(title="Urban Tasty SmartOps API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Urban Tasty SmartOps API"}

@app.get("/api/dashboard")
def get_dashboard():
    # Recalculate stats to reflect current mock_data state
    mock_data.dashboard_stats["total_orders"] = len(mock_data.orders)
    mock_data.dashboard_stats["low_stock_alerts"] = len([i for i in mock_data.inventory_list if i["status"] in ["Low Stock", "Critical"]])
    mock_data.dashboard_stats["staff_present"] = len([s for s in mock_data.staff_list if s["attendance"] == "Present"])
    mock_data.dashboard_stats["certifications_expiring"] = len([c for c in mock_data.certifications if c["status"] in ["Warning", "Critical"]])
    mock_data.dashboard_stats["revenue"] = sum([o["total"] for o in mock_data.orders if o["status"] != "Cancelled"])
    return mock_data.dashboard_stats

@app.get("/api/staff")
def get_staff():
    return mock_data.staff_list

@app.get("/api/inventory")
def get_inventory():
    return mock_data.inventory_list

@app.get("/api/certifications")
def get_certifications():
    return mock_data.certifications

@app.get("/api/orders")
def get_orders():
    return mock_data.orders

@app.get("/api/delivery")
def get_delivery():
    return mock_data.deliveries

@app.get("/api/products")
def get_products():
    return mock_data.products

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
