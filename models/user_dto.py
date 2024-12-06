from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class UserDto:
    azure_ad_id: str
    tenant_id: str
    email: str
    full_name: str
    user_id: Optional[str] = None
    created_at: Optional[datetime] = None
    last_login_at: Optional[datetime] = None


    def to_dict(self, include_none=False):
        """Return the object's attributes as a dictionary."""
        # Get all attributes as a dictionary
        attributes = {
            "azure_ad_id": self.azure_ad_id,
            "tenant_id": self.tenant_id,
            "email": self.email,
            "full_name": self.full_name,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "last_login_at": self.last_login_at,
        }
        
        # If include_none is False, filter out None values
        if not include_none:
            attributes = {k: v for k, v in attributes.items() if v is not None}
        
        return attributes