import unittest
from app import create_app


class TestUserEndpoints(unittest.TestCase):
    '''Unitest for UserEndPoints'''
    def setUp(self):
        """Initialize the app and client before each test"""
        self.app = create_app()
        self.client = self.app.test_client()

    # POST Tests
    def test_create_user_valid_data(self):
        """Test user creation with valid data"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get("error"), None)

    def test_create_user_invalid_first_name_none(self):
        """Test user creation with an empty first name"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "zdzdzd",
            "email": "zdzdzd@zd.zd"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "First name can only contain letters and spaces")

    def test_create_user_invalid_first_name_out_of_range(self):
        """Test user creation with a first name that's too long"""
        response = self.client.post('/api/v1/users/', json={
            "first_name":
            "zdzdzdzdzdzdzdzzddzdzdzdzdzdzdzdzdzdzdzdzdzdzdzdzdzzdzdz",
            "last_name": "Elodie",
            "email": "elo@elo.elo"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "First name must be present with a maximum"
                         " of 50 characters and can only"
                         " contain letters, spaces '-' and '''.")

    def test_create_user_invalid_first_name_bad_character(self):
        """Test user creation with invalid characters in the first name"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "zdzd$ù@",
            "email": "zdzd@zd.zd"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "First name format invalid.")

    def test_create_user_invalid_last_name_none(self):
        """Test user creation with an empty last name"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "zdzdzd",
            "last_name": "",
            "email": "zdzdzd@zd.zd"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "last name can't be empty")

    def test_create_user_invalid_last_name_out_of_range(self):
        """Test user creation with a first name that's too long"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "zdzdzd",
            "last_name":
            "zdzdzdzdzdzdzdzdzdzzdzdzdzdzdzdzdzzddzdzdzdzdzdzdzdzdzzd",
            "email": "zdzd@zd.zd"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "Last name must be present with a maximum of 50"
                         " characters and can only contain letters "
                         "and spaces.")

    def test_create_user_invalid_first_name_bad_character(self):
        """Test user creation with invalid characters in the first name"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "zdzdzdz",
            "last_name": "zdzdzdzd/@$",
            "email": "zdzd@zd.zd"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "Last name can only contain letters and spaces")

    def test_create_user_invalid_email_format(self):
        """Test user creation with an invalid email format"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "zdzd",
            "last_name": "zdzd",
            "email": "zdzd@zd."
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "The email format is invalid.")

    def test_create_user_invalid_email_none(self):
        """Test user creation with an invalid email format"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "zdzd",
            "last_name": "zdzd",
            "email": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "The email format is invalid.")


class TestAmenityEndpoints(unittest.TestCase):
    '''Unitest for AmenityEndPoints'''
    def setUp(self):
        """Initialize the app and client before each test"""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_amenity_create_valid(self):
        """Test amenity creation with valid data"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Terrasse"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get("error"), None)

    def test_amenity_create_name_none(self):
        """Test amenity creation with valid data"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "Amenity name must be a string "
                         "of 1 to 50 characters.")

    def test_amenity_create_name_oput_of_range(self):
        """Test amenity creation with valid data"""
        response = self.client.post('/api/v1/amenities/', json={
            "name": "zdzdzdzdzdzdzdzdzdzdzdzdzdzdz"
            "zzdzdzdzdzdzdzdzdzdzdzdzdzdzdzdzdzdzdzd"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "Amenity name must be a string "
                         "of 1 to 50 characters.")


class TestPlaceEndpoints(unittest.TestCase):
    '''Unitest for AmenityEndPoints'''
    def setUp(self):
        """Initialize the app and client before each test"""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_place_create_valid_data(self):
        """Test place creation with valid data"""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Johnny",
            "last_name": "Doee",
            "email": "john.doee@example.com"
        })
        self.assertEqual(user_response.status_code, 201)
        owner_id = user_response.json['id']

        response = self.client.post('/api/v1/places/', json={
            "title": "random house",
            "description": "cool view",
            "price": 265,
            "latitude": 98.27,
            "longitude": -67.56,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json.get("error"), None)

    def test_place_create_invalid_price(self):
        """Test place creation with valid data"""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        })
        self.assertEqual(user_response.status_code, 201)
        owner_id = user_response.json['id']

        response = self.client.post('/api/v1/places/', json={
            "title": "random house",
            "description": "cool view",
            "price": -456,
            "latitude": 67.28,
            "longitude": -78.64,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("error"),
                         "Price cannot be negative")

    def test_place_create_invalid_latitude(self):
        """Test place creation with invalid latitude"""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Jodzdzhn",
            "last_name": "Dodzze",
            "email": "johdzdzn.doe@example.com"
        })
        self.assertEqual(user_response.status_code, 201)
        owner_id = user_response.json['id']

        response = self.client.post('/api/v1/places/', json={
            "title": "random house",
            "description": "cool view",
            "price": 200,
            "latitude": 127.0,
            "longitude": -78.28,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get('error'),
                         "Latitude must be between -90.0 and 90.0")

    def test_place_create_invalid_longitude(self):
        """Test place creation with invalid longitude"""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Johen",
            "last_name": "Doee",
            "email": "johdzd.doe@example.com"
        })
        self.assertEqual(user_response.status_code, 201)
        owner_id = user_response.json['id']

        response = self.client.post('/api/v1/places/', json={
            "title": "random house",
            "description": "cool view",
            "price": 664,
            "latitude": 64.87,
            "longitude": -877.0,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get('error'),
                         "Longitude must be between -180.0 and 180.0")

    def test_place_create_invalid_user_id(self):
        """Test place creation with invalid longitude"""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Johdzen",
            "last_name": "Ddzdzoee",
            "email": "johdzdzedn.doe@example.com"
        })
        self.assertEqual(user_response.status_code, 201)
        owner_id = user_response.json['id']

        response = self.client.post('/api/v1/places/', json={
            "title": "random house",
            "description": "cool view",
            "price": 400,
            "latitude": 23.65,
            "longitude": 470.0,
            "owner_id": "1234567"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get('error'), None)


class TestReviewEndpoints(unittest.TestCase):
    '''Unitest for Review EndPoints'''
    def setUp(self):
        """Initialize the app and client before each test"""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_review_create_valid_data(self):
        """ Initialize place and user before every test."""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Johndzdzny",
            "last_name": "Dodxzdzee",
            "email": "john.dxdzdzoee@example.com"
        })
        self.assertEqual(user_response.status_code, 201)
        owner_id = user_response.json['id']

        place_response = self.client.post('/api/v1/places/', json={
            "title": "random house",
            "description": "cool view",
            "price": 400,
            "latitude": 89.67,
            "longitude": 89.67,
            "owner_id": owner_id
        })
        self.assertEqual(place_response.status_code, 201)
        place_id = place_response.json['id']

        review_response = self.client.post('/api/v1/reviews/', json={
            "text": "super cool house !",
            "user_id": owner_id,
            "place_id": place_id,
            "rating": 4
        })
        self.assertEqual(review_response.status_code, 201)

    def test_review_create_no_text(self):
        """ Initialize place and user before every test."""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Johndzddzzny",
            "last_name": "Dodxzddzzee",
            "email": "johndxdzdzdzoee@example.com"
        })
        self.assertEqual(user_response.status_code, 201)
        owner_id = user_response.json['id']

        place_response = self.client.post('/api/v1/places/', json={
            "title": "super cool view",
            "description": "cool house",
            "price": 400,
            "latitude": 89.67,
            "longitude": 89.67,
            "owner_id": owner_id
        })
        self.assertEqual(place_response.status_code, 201)
        place_id = place_response.json['id']

        review_response = self.client.post('/api/v1/reviews/', json={
            "text": "",
            "user_id": owner_id,
            "place_id": place_id,
            "rating": 4
        })
        self.assertEqual(review_response.status_code, 400)

    def test_review_create_invalid_user_id(self):
        """ Initialize place and user before every test."""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Johnddzddzzny",
            "last_name": "Dzodxzdddzzee",
            "email": "johndxzdzdzdzoee@example.com"
        })
        self.assertEqual(user_response.status_code, 201)
        owner_id = user_response.json['id']

        place_response = self.client.post('/api/v1/places/', json={
            "title": "splendid house",
            "description": "never seen",
            "price": 400,
            "latitude": 89.67,
            "longitude": 89.67,
            "owner_id": owner_id
        })
        self.assertEqual(place_response.status_code, 201)
        place_id = place_response.json['id']

        review_response = self.client.post('/api/v1/reviews/', json={
            "text": "Merci",
            "user_id": 123456,
            "place_id": place_id,
            "rating": 4
        })
        self.assertEqual(review_response.status_code, 400)

    def test_review_create_invalid_place_id(self):
        """ Initialize place and user before every test."""
        user_response = self.client.post('/api/v1/users/', json={
            "first_name": "Johzny",
            "last_name": "Dzodzee",
            "email": "zdzoee@example.com"
        })
        self.assertEqual(user_response.status_code, 201)
        owner_id = user_response.json['id']

        place_response = self.client.post('/api/v1/places/', json={
            "title": "splendid balcony view",
            "description": "super cool place",
            "price": 400,
            "latitude": 89.67,
            "longitude": 89.67,
            "owner_id": owner_id
        })
        self.assertEqual(place_response.status_code, 201)
        place_id = place_response.json['id']

        review_response = self.client.post('/api/v1/reviews/', json={
            "text": "Merci",
            "user_id": owner_id,
            "place_id": 123456,
            "rating": 4
        })
        self.assertEqual(review_response.status_code, 400)