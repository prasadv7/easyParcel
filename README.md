# EasyParcel

EasyParcel is a Django-based backend system for a peer-to-peer parcel delivery platform. This system provides a robust API with JWT-based authentication, modular architecture, and support for features like user registration, parcel tracking, notifications, and more.

---

## **Project Overview**

### **Features**
- **Authentication**: JWT-based user login and registration.
- **User Management**: Custom user model supporting roles like delivery agents.
- **Parcel Management**: Create, view, and manage parcel delivery requests.
- **Notifications**: Notify users about updates on their parcels.
- **Tracking**: Real-time tracking of parcel statuses.
- **Role-Based Access**: Protect resources and enforce permissions for users and delivery agents.

---

## **Setup Guide**

### **1. Clone the Repository**
```bash
git clone https://github.com/prasadv7/easyParcel.git
cd easyParcel
```

### **2. Create a Virtual Environment**
```bash
python -m venv env
```

- **Windows**:
  ```bash
  env\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source env/bin/activate
  ```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**
Create a `.env` file in the root directory and add:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### **5. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Run the Development Server**
```bash
python manage.py runserver
```

---

## **API Endpoints**

### **Authentication**

#### **Register**: `POST /api/register/`
- **Request Body**:
  ```json
  {
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "username": "testuser",
    "email": "test@example.com"
  }
  ```

#### **Login**: `POST /api/users/login/`
- **Request Body**:
  ```json
  {
    "username": "testuser",
    "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
    "access": "jwt_access_token",
    "refresh": "jwt_refresh_token"
  }
  ```

### **Parcels**

#### **List Parcels**: `GET /api/parcels/`
- **Description**: Retrieve a list of all parcels (requires authentication).

#### **Create Parcel**: `POST /api/parcels/`
- **Request Body**:
  ```json
  {
    "pickup_location": "Location A",
    "dropoff_location": "Location B",
    "description": "A small parcel"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "pickup_location": "Location A",
    "dropoff_location": "Location B",
    "description": "A small parcel",
    "status": "Pending"
  }
  ```

---

## **Modules Overview**

### **1. Users Module**
- **Purpose**: Handles user registration, login, and authentication.
- **Main Features**:
  - Custom user model with roles (`is_delivery_agent`).
  - JWT-based authentication.

### **2. Parcels Module**
- **Purpose**: Manage parcel delivery requests.
- **Main Features**:
  - Create, view, and update parcel details.
  - Assign parcels to delivery agents.

### **3. Notifications Module**
- **Purpose**: Send notifications for parcel updates.
- **Main Features**:
  - Email and push notifications for status changes.

### **4. Tracking Module**
- **Purpose**: Track the real-time status of parcels.
- **Main Features**:
  - GPS tracking integration (optional).
  - Status updates for users and agents.

---

## **Directory Structure**
```plaintext
easyParcel/
    backend/
        settings.py
        urls.py
        wsgi.py
        asgi.py
    users/
        models.py
        views.py
        serializers.py
        urls.py
    parcels/
        models.py
        views.py
        serializers.py
        urls.py
    notifications/
        ...
    tracking/
        ...
```

---

## **Future Enhancements**
1. **Subscription Plans**: Premium features for frequent users.
2. **Analytics**: Insights for admins (e.g., popular routes, delivery times).
3. **Role-Based Permissions**: Enhanced control for different user roles.

---

## **Contributing**
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to your fork:
   ```bash
   git push origin feature-branch
   ```
5. Submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.
