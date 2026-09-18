from dataclasses import dataclass

@dataclass(frozen=True)
class Permission:
    subject: str
    action: str
    resource: str = "*"

class PermissionManager:
    """Simple allow-list boundary for future RBAC/ABAC integration."""

    def __init__(self) -> None:
        self._permissions: set[Permission] = set()

    def grant(self, subject: str, action: str, resource: str = "*") -> None:
        self._permissions.add(Permission(subject, action, resource))

    def allowed(self, subject: str, action: str, resource: str = "*") -> bool:
        return Permission(subject, action, resource) in self._permissions or Permission(subject, action, "*") in self._permissions
