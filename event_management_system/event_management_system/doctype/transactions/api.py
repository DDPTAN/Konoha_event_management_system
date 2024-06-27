
import frappe
from frappe import ValidationError
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
        return {'error': error}
    
@frappe.whitelist()
def get_registered_count(event):
    transactions = frappe.db.count('Transactions', event)
    frappe.msgprint(transactions)
    return f'{transactions}'