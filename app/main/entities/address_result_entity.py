from dataclasses import dataclass


@dataclass(init=True, eq=True, frozen=True)
class AddressResultEntity:
    address1: str
    address2: str
    city: str
    state: str
    zip5: str
    zip4: str
