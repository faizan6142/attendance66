# View-Only Role Implementation

## Role: Viewer

### Permissions:
- Can view and download attendance records.
- Cannot add, update, or modify student information.
- Cannot perform any operations that modify attendance.

## Implementation Steps:
1. Define a new role named 'viewer' in the roles management system.
2. Set permissions for the 'viewer' role to allow read access to attendance data.
3. Ensure that all functions for student updates and attendance modifications check for the 'viewer' role and deny access accordingly.

## Code Changes:
```python
class AttendanceManagement:
    ...
    roles = ['admin', 'editor', 'viewer']

    def __init__(self):
        self.permissions = {
            'admin': {'add_students': True, 'update_students': True, 'modify_attendance': True},
            'editor': {'add_students': True, 'update_students': True, 'modify_attendance': False},
            'viewer': {'view_attendance': True, 'download_attendance': True}
        }
    
    def check_permission(self, role, action):
        ...
        if role == 'viewer' and action in ['add_students', 'update_students', 'modify_attendance']:
            return False
        return True
```  
```

## Testing:
- Test the `check_permission` function to ensure the viewer role correctly denies modifying actions while allowing viewing.
- Manually test the user interface to ensure the viewer role can view/download attendance without issues.
```
