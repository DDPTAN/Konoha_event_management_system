import frappe
import base64
from frappe import ValidationError
import io
from PIL import Image

@frappe.whitelist()
def create_transaction_for_user(event, total_payment, event_name):
    transaction = frappe.get_doc({
        'doctype': 'Transactions',
        'event': event,
        'total_payment': total_payment,
        
        
    })
    try:
        transaction.insert(ignore_permissions=True)
        return f'Kamu Sudah Berhasil Join Event {event_name}'
    except ValidationError as error:
        return {'error': str(error)}

@frappe.whitelist()
def get_registered_count(event):
    transactions_count = frappe.db.count('Transactions', {'event': event})
    frappe.msgprint(transactions_count)
    return f'{transactions_count}'

@frappe.whitelist()
def save_transaction_payment(transaction_name, file_url):
    
    try:
        transaction_doc = frappe.get_doc('Transactions', transaction_name)
        transaction_doc.payment_bill = file_url
        transaction_doc.status = 'Menunggu Konfirmasi'
        transaction_doc.save(ignore_permissions=True)

        return {'status': 'success', 'message': 'Berhasil upload bukti pembayaran'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
