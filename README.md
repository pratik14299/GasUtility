# GasUtility
GasUtility - ServiceRequest
GasUtility Service API Documentation
Introduction
Welcome to the GasUtility Service API documentation. This API allows users to manage customer service requests and customers for gas-related services.

Base URL
All endpoints described in this document are relative to the base URL of the application. The base URL is assumed to be: http://127.0.0.1:8000

Authentication
Authentication details and requirements are not provided in this example. Ensure to implement proper authentication mechanisms before deploying these APIs to a production environment.

API Endpoints
1. Service Requests
List all Service Requests
Endpoint: /servicerequests/
Method: GET
Description: Retrieve a list of all service requests.
Response:
Status: 200 OK
Body: List of service requests.
Create a New Service Request
Endpoint: /servicerequests/
Method: POST
Description: Create a new service request.
Request Body Example:
json
Copy code
{
    "account": 1,
    "customer": "Pratik",
    "Service_Type": "Gas Leak",
    "request_detials": "Gas Leak",
    "attachment": null,
    "submitted_at": "2023-08-18T04:56:37.291407Z"
}
Response:
Status: 201 Created
Body: Object with the tracking number for the created service request.
Track Service Request Status
Endpoint: /track/<tracking_no>/
Method: GET
Description: Get the status and resolved date of a specific service request.
Response:
Status: 200 OK
Body Example:
json
Copy code
{
    "tracking_no": "4cd6fe8c-1364-4d8e-9373-1f07a0987fcc",
    "statuses": [
        "Resolved"
    ],
    "resolved_date": "2023-08-18 09:45:07"
}
Response: Object with tracking number, statuses, and resolved date (if available).
2. Customers
List all Customers
Endpoint: /customers/
Method: GET
Description: Retrieve a list of all customers.
Response:
Status: 200 OK
Body: List of customers.
Create a New Customer
Endpoint: /customers/
Method: POST
Description: Create a new customer.
Response:
Status: 201 Created
3. Admin Panel
Add Tracking Status
Endpoint: /admin/app1/trackstatus/
Method: POST
Description: Add details of a service request to the TrackStatus model (Admin Panel only). Need to update at both ServiceRequest as well as trackstatus.
Request Body:
tracking_no: Tracking number of the service request.
status: Status of the service request.
resolved_at: Resolved date of the service request (optional).
Response:
Status: 201 Created
Body: Object with the created tracking status details.
Update Tracking Status
Endpoint: /admin/update_tracking_status/<int:pk>/
Method: PATCH
Description: Update the status and resolved date of a service request in the TrackStatus model (Admin Panel only).
Request Body:
status: Updated status of the service request.
resolved_at: Updated resolved date of the service request (optional).
Response:
Status: 200 OK
Body: Object with the updated tracking status details.


Conclusion
This document outlines the available APIs for the GasUtility Service. Users can use these endpoints to manage service requests and customers, and track the status of their service requests. Admins can use the Admin Panel endpoints to add and update tracking status details. Ensure proper authentication and authorization mechanisms are implemented before deploying these APIs to a production environment.
