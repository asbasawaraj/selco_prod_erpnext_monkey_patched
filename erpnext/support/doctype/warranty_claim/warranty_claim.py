# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


from __future__ import unicode_literals
import frappe
from frappe import session, _
from frappe.utils import today



from erpnext.utilities.transaction_base import TransactionBase

class WarrantyClaim(TransactionBase):
	def get_feed(self):
		return _("{0}: From {1}").format(self.status, self.customer_name)

	def validate(self):
		if session['user'] != 'Guest' and not self.customer:
			frappe.throw(_("Customer is required"))

		if self.status=="Closed" and \
			frappe.db.get_value("Warranty Claim", self.name, "status")!="Closed":
			self.resolution_date = today()
			#Start of entering data by Poorvi on September 23
			"""		if self.workflow_state == "Warranty Claim Format Raised - WC":
			if self.selco_panel:
				if not self.selco_panel_capacity:
				#frappe.errprint("Please Enter Service Person Name")
					frappe.throw("Please Enter Panel Capacity ")
				if not self.panel_serial_number:
					frappe.throw("Please Enter Panel Serial Number ")
				if not self.selco_panel_make:
					frappe.throw("Please Enter Panel Make ")
				if not self.selco_within_warranty:
					frappe.throw("Please Enter  Within Warranty ")
				if not self.selco_technical_information:
					frappe.throw("Please Enter Technical Information ")
			if self.selco_battery:
				if not self.selco_battery_capacity:
					frappe.throw("Please Enter Battery Capacity ")
				if not self.selco_battery_serial_number:
					frappe.throw("Please Enter Battery Serial Number ")
				if not self.selco_battery_supplier:
					frappe.throw("Please Enter Battery supplier ")
				if not self.selco_battery_within_warranty:
					frappe.throw("Please Enter Battery Within Warranty ")
			if self.selco_inverter:
				if not self.selco_inverter_capacity:
					frappe.throw("Please Enter Inverter Capacity ")
				if not self.selco_inverter_serial_number:
					frappe.throw("Please Enter Inverter Serial Number ")
				if not self.selco_inverter_make:
					frappe.throw("Please Enter Inverter Make ")
				if not self.selco_inverter_within_warranty:
					frappe.throw("Please Enter Inverter Within Warranty ")
			if self.selco_water_heater:
				if not self.selco_water_heater_capacity:
					frappe.throw("Please Enter Water Heater Capacity ")
				if not self.selco_water_heater_make:
					frappe.throw("Please Enter Water Heater Make ")
				if not self.selco_type_of_water_heater:
					frappe.throw("Please Enter Type Of Water Heater ")
			if self.selco_fan_luminary_others:
				if not self.selco_capacity1:
					frappe.throw("Please Enter Capacity ")
				if not self.selco_serial_number1:
					frappe.throw("Please Enter Serial Number ")
				if not self.selco_fan_luminery_make1:
					frappe.throw("Please Enter Fan Luminary Make")"""
				#End of entering data  By Poorvi
		#Start of Inser By Basawaraj on 9th Nov For Ticket #1 in BitBucket/Customization
		if self.workflow_state =="Dispatched From Godown":
			self.status = "Closed"
		#End of Inser By Basawaraj on 9th Nov For Ticket #1 in BitBucket/Customization

	def on_cancel(self):
		lst = frappe.db.sql("""select t1.name
			from `tabMaintenance Visit` t1, `tabMaintenance Visit Purpose` t2
			where t2.parent = t1.name and t2.prevdoc_docname = %s and	t1.docstatus!=2""",
			(self.name))
		if lst:
			lst1 = ','.join([x[0] for x in lst])
			frappe.throw(_("Cancel Material Visit {0} before cancelling this Warranty Claim").format(lst1))
		else:
			frappe.db.set(self, 'status', 'Cancelled')

	def on_update(self):
		if self.workflow_state == "Wrranty Claim Format Raised - WC":
			doc = frappe.get_doc("Issue", self.complaint_number)
			doc.db_set('warranty_claim_format', self.name)
			frappe.db.commit()


@frappe.whitelist()
def make_maintenance_visit(source_name, target_doc=None):
	from frappe.model.mapper import get_mapped_doc, map_child_doc

	def _update_links(source_doc, target_doc, source_parent):
		target_doc.prevdoc_doctype = source_parent.doctype
		target_doc.prevdoc_docname = source_parent.name

	visit = frappe.db.sql("""select t1.name
		from `tabMaintenance Visit` t1, `tabMaintenance Visit Purpose` t2
		where t2.parent=t1.name and t2.prevdoc_docname=%s
		and t1.docstatus=1 and t1.completion_status='Fully Completed'""", source_name)

	if not visit:
		target_doc = get_mapped_doc("Warranty Claim", source_name, {
			"Warranty Claim": {
				"doctype": "Maintenance Visit",
				"field_map": {}
			}
		}, target_doc)

		source_doc = frappe.get_doc("Warranty Claim", source_name)
		if source_doc.get("item_code"):
			table_map = {
				"doctype": "Maintenance Visit Purpose",
				"postprocess": _update_links
			}
			map_child_doc(source_doc, target_doc, table_map, source_doc)

		return target_doc
