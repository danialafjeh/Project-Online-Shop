# 💻 About This Project

[Complete Guide | Run this project on your computer](https://github.com/danialafjeh/Run-My-Projects-Locally)<br>

# Pharmacy E-Commerce/Online Shop Website

Complexity : Advanced

A pharmacy e-commerce web application with frontend and backend developed using **Django MVT architecture** for the backend and a stylish responsive frontend built with **HTML, CSS, SCSS, and JavaScript**. (Because my specialization is backend development, the UI is based on a Bootstrap template from templatemo.com to achieve a neat, responsive design.)

The project focuses heavily on backend development, authentication systems, database management, and role-based access control while also providing a clean and modern user interface. so frontend is made with customized and ready made template.

## Features

* Advanced product search functionality
* Complete online shopping experience:
  - Shopping cart
  - Order placement
  - Order tracking
  - Orders history
  - Order cancellation
* Product categories and brand filtering system
* Browse all products with dynamic filters
* Pharmacy products organized by categories and brands
* Pharmacy and doctor information stored dynamically in the database
* Dedicated About Us and Doctor Information pages
* Secure authentication and authorization system
* User registration, login, and logout system
* Modern and responsive authentication forms
* Separate authentication system for administrators and customers
* Role-based access levels and permissions



### Database & ORM Optimization
- Database indexing on frequently queried fields to improve filtering and lookup performance.
- Optimized ORM queries using `select_related()` to minimize unnecessary database queries and prevent N+1 query problems.
- Efficient database access patterns through direct access to authenticated user instances and foreign key references.
- Optimized cart calculations by eliminating unnecessary nested iterations and retrieving only the required database fields.
- Refined model field definitions and database schema management through Django migrations.

### Transactional Integrity & Order Processing
- Implementation of `transaction.atomic()` throughout the order creation workflow to ensure that order records, order items, and related database updates are handled as a single atomic operation.
- Transactional consistency with automatic rollback in case of failures, preventing partially persisted orders.
- Optimized product retrieval and quantity lookups during order processing.
- Separation of session-based cart operations from database transactions to prevent premature session updates when a transaction fails.
- Consistent order lifecycle management while maintaining clear separation between order creation and payment processing.

### Security & Authorization
- User-specific ownership validation to ensure that customers can only access and manage their own orders.
- Server-side retrieval of delivery information based on the authenticated user rather than relying on client-submitted identifiers.
- Secure authorization checks across order tracking, cancellation, and order detail views.
- Consistent authentication and access-control handling throughout protected application workflows.

### Redis Caching & Cache Invalidation
- Redis integration through `django-redis` as the application's caching backend.
- Strategic caching of frequently accessed public-facing pages and database-driven content.
- Shared cache entries across views that depend on identical underlying data, reducing redundant database queries.
- Storage of evaluated query results to avoid caching lazy QuerySets.
- Automatic cache invalidation through Django model signals (`post_save` and `post_delete`).
- Transaction-aware cache invalidation using `transaction.on_commit()` to ensure cache entries are cleared only after successful database transactions.
- Centralized cache invalidation for products, categories, brands, and pharmacy information.
- A configurable 15-minute cache expiration policy.

### Cart Management & Application Architecture
- Session-based shopping cart management with database synchronization for authenticated users.
- JSON-based cart serialization using Python's standard `json` module.
- Optimized product retrieval and total price calculations.
- Reduced redundant database operations during cart synchronization and order processing.
- Separation of cart management, order processing, and application responsibilities for improved maintainability.

### Docker & Containerization
- Containerized Django application using a custom Dockerfile.
- Docker Compose orchestration for the Django application and Redis services.
- Persistent SQLite database storage through host-mounted volumes, preserving application data across container rebuilds and restarts.
- Persistent Redis storage through Docker-managed volumes.
- Automated database migrations during container startup through a dedicated `entrypoint.sh` script.
- Application execution through Django's standard `manage.py runserver` command.
- Environment-based configuration managed directly through Docker Compose.
- UTF-8 support and Linux-compatible line endings for container startup scripts.
- Dedicated `.dockerignore` and `.gitignore` configurations for clean build contexts and repository management.

### Code Quality & Maintainability
- Consistent code organization and separation of concerns across application components.
- Efficient database access patterns and reduced redundant operations.
- Maintainable model, view, and transaction structures.
- Consistent application behavior across refactored workflows.
- Database schema consistency maintained through Django's migration system.

**Database Note 1 :** The application currently uses SQLite. Database operations requiring transactional consistency are handled through `transaction.atomic()`. Since the current order workflow does not include concurrent inventory deduction or real payment processing, row-level locking through `select_for_update()` is not required by the present business logic.

**Database Note 2 :**The project uses SQLite as its database engine. Since SQLite is a file-based database, the database is maintained as a single file (`db.sqlite3`) within the repository and is included in version control.

This approach ensures that the application's initial data, including products, categories, brands, pharmacy information, and other store-related content, remains consistent across different environments. Whether the project is launched locally or through Docker, on any supported system, the same predefined store data is available without requiring a separate database setup or manual data population.

For Docker deployments, the existing SQLite database file is mounted into the container, allowing the application to use the same database while keeping its data persistent outside the container lifecycle.

All existing user accounts, customer information, orders, and other records are demo data created exclusively for testing and demonstration purposes. No real customer information or production user data is included in the repository.

## Customer Dashboard Features

Customers have access to a dedicated and modern profile dashboard with features such as:

* Viewing and editing account information
* Managing shipping information, phone numbers, and addresses
* Viewing and tracking registered orders
* Clean and user-friendly profile interface

---

## Admin Dashboard Features

Administrators have access to a powerful management panel with advanced permissions, including:

* Managing all users and customer accounts
* Managing products and pharmacy information
* Managing doctor information
* Managing brands and product categories
* Viewing and managing all registered orders
* Editing and deleting website data
* Access to the full Django administration panel
* Admin dashboard is Django's admin panel but with fully customized looking 

## Technologies Used

* Django (MVT Architecture)
* HTML5
* CSS3
* SCSS
* JavaScript
* SQLite / Django ORM

## Project Purpose

The goal of this project was to build a complete and scalable online pharmacy platform with secure authentication, professional dashboard systems, advanced admin management features, and a modern shopping experience using Django.

