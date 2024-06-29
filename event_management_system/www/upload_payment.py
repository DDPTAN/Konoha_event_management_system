import frappe
from frappe import _

def get_context(context):
    # Ambil parameter transaction_id dari URL
    transaction_name = frappe.form_dict.transaction_name
    if not transaction_name:
        frappe.throw(_("Transaction ID is required"))
    
    # Tambahkan transaction_id ke konteks
    context.transaction_name= transaction_name
    return context