// Copyright (c) 2024, team konoha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Events", {
	category(frm) {
		var doc = frm.doc;

		if (doc.category == "Gratis") {
			frm.set_df_property("price", "hidden", 1);
			frm.refresh_field("price");
			frappe.msgprint("Kategori Gratis dipilih");
		} else if (doc.category == "Berbayar") {
			frm.set_df_property("price", "hidden", 0);
			frm.refresh_field("price");
			frappe.msgprint("Silahkan isi harga/Price Event");
		} else {
			frappe.msgprint("Error");
		}
	},

	date(frm) {
		let currentDate = new Date();
		let setDate = new Date(frm.doc.date);
		if (setDate <= currentDate) {
			frm.set_value("date", "");
			frappe.throw("Tanggal Sudah Lewat");
		}
	},

	before_save(frm) {
		var doc = frm.doc;
		if (doc.capacity === 0) {
			frappe.throw("Capacity tidak boleh 0");
		}

		if (doc.category === "Berbayar") {
			if (doc.price === 0) {
				frappe.throw("Event Berbayar - Harga tidak boleh 0");
			}
		}
	},
});
