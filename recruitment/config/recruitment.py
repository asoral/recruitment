from frappe import _


def get_data():
    return [
        {
            "module_name": "Recruitment",
            "color": "grey",
            "icon": "fa fa-star",
                    "type": "module",
                    "label": _("Recruitment"),
                    "items": [
                        {
                            "type": "doctype",
                            "name": "Candidate",
                            "icon": "fa fa-star",
                            "label": _("Candidate"),
                            "description": _("VHRS Candidate Database"),
                        },
                        {
                            "type": "doctype",
                            "name": "Closure",
                            "icon": "fa fa-star",
                            "label": _("Closure"),
                            "description": _("Recruitment Documentation"),
                        },
                        {
                            "type": "doctype",
                            "name": "Interview",
                            "label": _("Interview"),
                            "description": _("Interviews for Projects"),
                        },
                        {
                            "type": "page",
                            "name": "dkb-dashboard",
                            "label": _("DKB Dashboard"),
                            "description": _("VHRS Candidate Database"),
                        },
                        {
                            "type": "page",
                            "name": "buhr-i-dashboard",
                            "label": _("BUHR-I Dashboard"),
                            "description": _("VHRS Candidate Database"),
                        },
                        {
                            "type": "doctype",
                            "name": "Associate",
                            "label": _("Associate"),
                            "description": _("VHRS Associate Database"),
                            "hide_count": False
                        }
                    ]
        }
    ]
