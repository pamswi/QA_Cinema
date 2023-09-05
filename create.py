from application import db, app
from models import User, Movie


with app.app_context():
    db.drop_all()
    db.create_all()

    test_user = User(
            username='testuser',
            email='testuser@example.com',
            password='password123',
            address='123 Test St',
            first_name='Test',
            last_name='User',
            card_number='1234567890123456',
            card_expiry='12/24',
            card_cvc=123
        )
    db.session.add(test_user)
    db.session.commit()