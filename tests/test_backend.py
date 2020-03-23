import unittest

from flask import abort, url_for
from flask_testing import TestCase

from application import app, db
from application.models import Hobby, Location
class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@35.246.103.66/tag_along')
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # register a plan
        locationData = Location(l_name = "Spain", time = "June")
        db.session.add(locationData)
        db.session.commit()
        l_id = Location.query.filter_by(l_id=locationData.l_id).first()
        hobbyData = Hobby(name = "Jane", h_name = "Hiking", email = "jane@gmail.com", plans = l_id)


        # save plan to database
        db.session.add(hobbyData)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


'''def test_postpage_view(self):
        target_url = url_for('post')
        redirect_url = url_for('login',next=target_url)
        response = self.client.get(url_for('post'))
        self.assertRedirects(response,redirect_url)'''