frappe.ui.form.on("Directory" ,{
	onload :function(cur_frm) {
		if (cur_frm.doc.__islocal){
			cur_frm.set_value("bod", [
				{ "designation": "President Elect"},
				{ "designation": "Treasurer"},
				{ "designation": "Director Club Service"},
				{ "designation": "Director Community Service"},
				{ "designation": "Director Vocational Service"},
				{ "designation": "Director International Service"},
				{ "designation": "Director Youth Services"},
				{ "designation": "Director Public Relations"},
				{ "designation": "Chairman TRF Support"},
				{ "designation": "Chairman Thrust Areas"},
				{ "designation": "Club Trainer"},
				{ "designation": "Director Membership Development"}
			]);
		}
	}
});	