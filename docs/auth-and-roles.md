# Auth and Roles

The community edition exposes a simple JWT auth flow:

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`

Roles:

- `user`: can access demo dashboard, review, reports, and profile.
- `admin`: can also access user management and data governance.

The backend uses `get_current_user` and `require_admin` dependencies. The frontend stores the JWT in local storage and protects `/app/*` routes.
