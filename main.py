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

@app.get("/api/ai-insights")
def get_ai_insights():
    insights = []
    
    # Inventory Insights
    low_stock = [i["name"] for i in mock_data.inventory_list if i["status"] in ["Low Stock", "Critical", "Warning"]]
    if low_stock:
        insights.append({
            "type": "inventory",
            "priority": "high",
            "message": f"Critical Stock Alert: {', '.join(low_stock[:2])} levels are below 15%. Order replenishment suggested within 24h.",
            "action": "Restock Now"
        })
    
    # Staffing Insights
    absent_staff = [s["name"] for s in mock_data.staff_list if s["attendance"] == "Absent"]
    if absent_staff:
        insights.append({
            "type": "staffing",
            "priority": "medium",
            "message": f"Staff Shortage: {len(absent_staff)} members absent today ({', '.join(absent_staff)}). Consider reassignment for peak hours.",
            "action": "View Schedule"
        })
    
    # Certification Insights
    expiring = [c["name"] for c in mock_data.certifications if c["status"] in ["Warning", "Critical"]]
    if expiring:
        insights.append({
            "type": "compliance",
            "priority": "high",
            "message": f"Compliance Risk: {expiring[0]} expires soon. Failure to renew may lead to operational pause.",
            "action": "Renew Now"
        })
    
    # Operational Pulse (Predictive)
    pending_orders = len([o for o in mock_data.orders if o["status"] == "Pending"])
    if pending_orders > 0:
        insights.append({
            "type": "operational",
            "priority": "medium",
            "message": f"Peak Demand: {pending_orders} orders are pending. Kitchen output is at 85% capacity.",
            "action": "Optimize Flow"
        })
    else:
        insights.append({
            "type": "operational",
            "priority": "low",
            "message": "Operations are stable. No immediate bottlenecks detected for the next 4 hours.",
            "action": "Systems Check"
        })

    return insights

@app.get("/api/products")
def get_products():
    return mock_data.products

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
