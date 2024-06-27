# Copyright (c) 2024, konoha and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import now_datetime, nowdate, getdate
from frappe.website.website_generator import WebsiteGenerator

class Transactions(WebsiteGenerator):
    def before_insert(self):
        self.check_event_category()
        self.check_event_is_registered()
        self.check_capacity_event()
        self.check_date_event()
        # self.set_event_details()
        
    def after_insert(self):
          self.update_event_capacity_free()
          
    def after_update(self):
        self.update_event_capacity_paid()

     # New method to set event details
    # def set_event_details(self):
    #     event = frappe.get_doc("Events", self.event)
    #     self.event_poster = event.event_poster
    #     self.organizer = event.organizer

     # existing methods...
    # def check_event_category(self):
    #     event = frappe.get_doc("Events", self.event)
    #     event_category = event.category
    #     if event_category.lower() == 'gratis':
    #         self.status = 'Dikonfirmasi'
    #     else:
    #         self.status = 'Menunggu Konfirmasi'
    #     self.user = frappe.session.user
    #     self.date = now_datetime()
        
	#before_insert
    def check_event_category(self):
        
        event = frappe.get_doc("Events", self.event)
        
        event_category = event.category
        
        if event_category.lower() == 'gratis':
            self.status = 'Dikonfirmasi'
        else:
            self.status = 'Menunggu Konfirmasi'
        
        self.user = frappe.session.user
        self.date = now_datetime()
        
    def check_capacity_event(self):
         event = frappe.get_doc("Events", self.event)
         transactions = frappe.db.count('Transactions', self.event)
         if event.capacity <= 0:
              frappe.throw(f'Kuota Event {event.event_name} Sudah Terpenuhi')
              
    def check_date_event(self):
          event = frappe.get_doc("Events", self.event)
          event_date = getdate(event.date)
          current_date = getdate(nowdate())
          if event_date < current_date:
               frappe.throw(f'Pendaftaran Event {event.event_name} Sudah Tertutup')
        
              
    def check_event_is_registered(self):
        existing_transaction = frappe.get_all(
            'Transactions', 
            filters={
                'event': self.event, 
                'user': self.user,
                # 'event_poster': self.event_poster,
                # 'organizer': self.organizer
            },
            limit=1
        )
        
        event = frappe.get_doc("Events", self.event)
        
        if existing_transaction:
            frappe.throw(f'Kamu Sudah Terdaftar Pada Event {event.event_name}')
            
    def update_event_capacity_free(self):
        event = frappe.get_doc("Events", self.event)
        if event.category == 'Gratis':
            event.capacity -= 1
        event.save(ignore_permissions=True)
        
    def update_event_capacity_paid(self):
        event = frappe.get_doc("Events", self.event)
        if self.status == 'Dikonfirmasi':
            event.capacity -= 1
            event.save(ignore_permission=True)

    
				
        
            
            
        