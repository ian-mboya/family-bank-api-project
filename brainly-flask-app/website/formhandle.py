from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import Payments, Student
import requests




formhandle = Blueprint('formhandle', __name__)


@formhandle.route('/submit', methods=['POST'])
def submit():
    student_id = request.form['student_id']
    fee_amount = request.form['fee_amount']
    payment_reason = request.form['payment_reason']
    payment_method = request.form['payment_method']

    # Validate student ID
    if not validate_student_id(student_id):
        flash('Invalid student ID!', 'danger')
        return redirect(url_for('index'))

    # Send data to external API
    payload = {
        'student_id': student_id,
        'amount': fee_amount,
        'payment_reason': payment_reason,
        'payment_method': payment_method
    }
    response = requests.post('https://external-api-url.com/endpoint', json=payload)

    if response.status_code == 200:
        api_response = response.json()
        if api_response.get('status') == 'success':
            # Add the payment to the local database
            new_payment = Payments(
                student_id=student_id,
                fee_amount=fee_amount,
                payment_reason=payment_reason,
                payment_method=payment_method
            )
            db.session.add(new_payment)
            db.session.commit()
            flash('Payment submitted successfully!', 'success')
        else:
            flash('Failed to submit payment: ' + api_response.get('message', 'Unknown error'), 'danger')
    else:
        flash('Failed to connect to the API', 'danger')

    return redirect(url_for('index'))

def validate_student_id(student_id):
    # Example validation against a hypothetical students table
    student = db.session.execute(db.select(Student).filter_by(student_id=student_id)).scalar_one_or_none()
    return student is not None
