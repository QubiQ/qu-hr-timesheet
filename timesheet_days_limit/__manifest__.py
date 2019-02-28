# Copyright 2019 Joan Segui <joan.segui@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Timesheet Days Limit",
    "summary": "Limit imputations in the timesheet by employee.",
    "version": "11.0.1.0.0",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "website": "https://www.qubiq.es",
    "category": "Timesheet",
    "license": "AGPL-3",
    "depends": [
        "hr",
        "project",
        "hr_timesheet",
    ],
    "data": [
        "views/hr_employee_view.xml",
    ],
    'installable': True,
    'application': False,
}
