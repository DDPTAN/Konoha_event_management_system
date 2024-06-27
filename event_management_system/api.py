# import frappe

# @frappe.whitelist()
# def register_event(event_name):
#     try:
#         user = frappe.session.user
#         doc = frappe.get_doc("Events", event_name)
#         if not frappe.db.exists("Registered Event", {"event_name": event_name, "user": user}):
#             frappe.get_doc({
#                 "doctype": "Registered Event",
#                 "event_name": event_name,
#                 "user": user
#             }).insert()
#             return "success"
#         else:
#             return "already_registered"
#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), 'Event Registration Error')
#         return "error"

