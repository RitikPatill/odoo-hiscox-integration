from odoo import models, fields, api
from ..services.qr_generator import generate_qr_code
from ..services.logger import log_error
from ..services.hiscox_api import submit_to_hiscox, check_status_from_hiscox


class HiscoxCase(models.Model):
    _name = "edited.hiscox.case"
    _description = "Hiscox Application Case"

    name = fields.Char(string="Customer Name", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone", required=True)
    application_status = fields.Selection([
        ('pending', 'Pending'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string="Application Status", default="pending")

    qr_code = fields.Binary(string="QR Code")

    @api.model
    def create(self, vals):
        """Generate QR code upon record creation."""
        try:
            qr_data = f"{vals.get('name')}|{vals.get('email')}|{vals.get('phone')}"
            vals['qr_code'] = generate_qr_code(qr_data)
        except Exception as e:
            log_error(f"QR Code generation failed: {str(e)}")
        return super(HiscoxCase, self).create(vals)

    # -------------------------------------------------------
    # Button-Based Workflow Methods
    # -------------------------------------------------------

    def action_submit(self):
        """
        Call the Hiscox API to submit the case.
        If successful, set status to 'submitted'.
        """
        try:
            response = submit_to_hiscox(self)
            if response:
                self.application_status = 'submitted'
            else:
                log_error("Failed to submit to Hiscox (no response or invalid response).")
        except Exception as e:
            log_error(f"Failed to submit to Hiscox: {str(e)}")

    def action_approve(self):
        """
        Approve the case manually.
        (No API call here, but you can add one if needed.)
        """
        self.application_status = 'approved'

    def action_reject(self):
        """
        Reject the case manually.
        (No API call here, but you can add one if needed.)
        """
        self.application_status = 'rejected'

    def action_check_status(self):
        """
        Query the Hiscox API for the current status of this case.
        If a new status is returned, update our record accordingly.
        """
        try:
            new_status = check_status_from_hiscox(self.id)
            if new_status:
                self.application_status = new_status
        except Exception as e:
            log_error(f"Failed to check status from Hiscox: {str(e)}")
