```mermaid
erDiagram
    TOURIST_SPOTS ||--o{ TOURS : has
    TOURIST_SPOTS ||--o{ REVIEWS : has
    TOURIST_SPOTS ||--o{ SPOT_TRANSPORT_LINKS : links
    TOURIST_SPOTS ||--o{ LOCAL_SHOPS : has
    TOURIST_SPOTS ||--o{ EMERGENCY_CONTACTS : has
    TOURIST_SPOTS ||--o{ ACCOMMODATIONS : has
    TOURS ||--o{ TOUR_GUIDE_ASSIGNMENTS : assigns
    TOURS ||--o{ BOOKINGS : booked
    TOURS ||--o{ DISCOUNTS : offers
    TOUR_GUIDES ||--o{ TOUR_GUIDE_ASSIGNMENTS : assigned
    CUSTOMERS ||--o{ BOOKINGS : books
    CUSTOMERS ||--o{ REVIEWS : reviews
    BOOKINGS ||--o{ ONLINE_PAYMENT : pays
    BOOKINGS ||--o{ ACCOMMODATION_BOOKINGS : reserves
    ACCOMMODATIONS ||--o{ ACCOMMODATION_BOOKINGS : reserved
    TRANSPORTATION ||--o{ SPOT_TRANSPORT_LINKS : links
```