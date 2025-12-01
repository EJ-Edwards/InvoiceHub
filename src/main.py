from fastapi import FastAPI
from models import ReceiptRequest
from service import calculate_receipt
from database import save_receipt, get_receipt

app = FastAPI(
    title="InvoiceHub",
    description="A simple API that generates receipts with totals & tax",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "InvoiceHub API is running!"}

@app.post("/receipt")
def create_receipt(data: ReceiptRequest):
    receipt = calculate_receipt(data)
    save_receipt(receipt)
    return receipt

@app.get("/receipt/{receipt_id}")
def fetch_receipt(receipt_id: str):
    receipt = get_receipt(receipt_id)
    if receipt is None:
        return {"error": "Receipt not found"}
    return receipt
