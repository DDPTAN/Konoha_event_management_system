import frappe

@frappe.whitelist(allow_guest=True)
def register_user(full_name, email, password):
    if not frappe.db.exists('User', email):
        user = frappe.new_doc('User')
        user.email = email
        user.first_name = full_name
        user.username = email
        user.enabled = 1
        user.new_password = password
        user.flags.ignore_permissions = True
        user.insert()
        
        user.add_roles('Member')
        frappe.msgprint('User registered successfully', 'Success')
        return {
            'status': 'success',
            'message': 'User registered successfully'
            }
    else:
        return {
            'status': 'error',
            'message': 'Email already registered'
        }
# def assign_role_to_user(doc, method):
#     # Definisikan role yang ingin ditambahkan
#     doc.role_profile_name = "Member"
#     doc.save(ignore_permissions=True)