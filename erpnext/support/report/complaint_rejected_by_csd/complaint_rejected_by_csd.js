// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Complaint Rejected By CSD"] = {
	"filters": [
		{
				"fieldname":"ss",
				"label": __("Service Branch"),
				"fieldtype": "Select",
				"options": "bangalore_service_center@selco-india.com\nbellary_service_center@selco-india.com\nchitradurga_service_center@selco-india.com\ndharwad_service_center@selco-india.com\nhassan_service_center@selco-india.com\nkundapura_service_center@selco-india.com\nmysore_service_center@selco-india.com\nputtur_service_center@selco-india.com\nshimoga_service_center@selco-india.com\nvijayapura_service_center@selco-india.com\n",
		},
		{
	"fieldname": "fiscal_year",
	"label": __("Fiscal Year"),
	"fieldtype": "Link",
	"options": "Fiscal Year",
	default: "2016-2017"
	},
	{
		"fieldname":"month_number",
		"label": __("Month"),
		"fieldtype": "Select",
		"options": "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec",
		"default": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
			"Dec"][frappe.datetime.str_to_obj(frappe.datetime.get_today()).getMonth()],
	}
]
}
