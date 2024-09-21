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