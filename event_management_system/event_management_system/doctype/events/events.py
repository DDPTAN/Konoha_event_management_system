import frappe
from frappe.website.website_generator import WebsiteGenerator

class Events(WebsiteGenerator):
    pass

@frappe.whitelist()


# def get_context(context):
#     # Ambil data acara dari dokumen "Events"
#     events = frappe.get_all('Event', fields=[ 'event_name', 'organizer', 'date', 'category', 'capacity', 'price', 'description'])

#     for event in events:
#         # Misalnya, kita gunakan contoh pengecekan berdasarkan nama acara atau logika bisnis tertentu
#         if is_event_registered(event['event_name']):
#             event['status'] = 'Terdaftar'
#         else:
#             event['status'] = 'Belum Terdaftar'

#     # Tetapkan data acara yang telah diproses ke dalam dictionary konteks
#     context.events = events

def register_event(event_name):
    try:
        # Lakukan validasi atau operasi lain yang diperlukan sebelum pendaftaran

        # Misalnya, buat dokumen pendaftaran baru atau tambahkan ke dalam tabel terkait
        # Misalkan, tambahkan peserta baru pada event
        event_doc = frappe.get_doc('Event', event_name)
        participant = frappe.new_doc('Event Participant')
        participant.event = event_name
        participant.user = frappe.session.user  # User yang sedang login
        participant.save()

        # Update status pendaftaran acara menjadi Terdaftar
        event_doc.status = 'Terdaftar'
        event_doc.save()

        return 'success'
    except Exception as e:
        frappe.log_error(_('Failed to register event: {0}').format(event_name), e)
        return 'error'
	
		
# class Events(WebsiteGenerator):
#     def get_context(self, context):
#         user = frappe.session.user
#         registered_events = [d.event_name for d in frappe.get_all("Registered Event", filters={"user": user}, fields=["event_name"])]
#         context.events = frappe.get_all("Events", filters={"name": ["not in", registered_events]}, fields=["*"])
#         return context

