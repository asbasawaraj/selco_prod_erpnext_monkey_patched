// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Complaint Budget"] = {
	"filters": [
		{
				"fieldname":"branch",
				"label": __("Branch"),
				"fieldtype": "Link",
				"options": "Branch"
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
	},
	{
			"fieldname":"selco_service_person",
			"label": __("Service Person"),
			"fieldtype": "Link",
			"options": "Service Person"
	}
	]
}

/*
frappe.query_reports["Complaint Budget"] = {
	"filters": [
		{
				"fieldname":"branch",
				"label": __("Branch"),
				"fieldtype": "Link",
				"options": "Branch"
		},
		{
	"fieldname": "from_date",
	"label": __("From Date"),
	"fieldtype": "Date",
	"default": frappe.defaults.get_user_default("month_start_date"),
},
{
	"fieldname": "to_date",
	"label": __("To Date"),
	"fieldtype": "Date",
	"default": frappe.defaults.get_user_default("month_start_date_end_date"),
},
	]
}

// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Complaint Budget"] = {
	"filters": [
		{
				"fieldname":"branch",
				"label": __("Branch"),
				"fieldtype": "Link",
				"options": "Branch"
		},
		{
	"fieldname": "fiscal_year",
	"label": __("Fiscal Year"),
	"fieldtype": "Link",
	"options": "Fiscal Year"
	},
	{
		"fieldname": "month",
		label: __("Period"),
		fieldtype: "Number",
		options: [
			{ "value": 01, "label": __("January") },
			{ "value": 02, "label": __("February") },
			{ "value": 03, "label": __("March") },
			{ "value": 04, "label": __("April") },
			{ "value": 05, "label": __("May") },
			{ "value": 06, "label": __("June") },
			{ "value": 07, "label": __("July") },
			{ "value": 08, "label": __("August") },
			{ "value": 09, "label": __("September") },
			{ "value": 10, "label": __("October") },
			{ "value": 11, "label": __("November") },
			{ "value": 12, "label": __("December") }
		],
	},
	]
}

*/
