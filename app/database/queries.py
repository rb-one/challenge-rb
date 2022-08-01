filters = ''

base_query = f"""
    SELECT p.address, p.city, s.name AS state, p.price, p.description, p.year
    FROM (
        SELECT sh.id, sh.property_id, sh.status_id, max(sh.update_date)
        FROM habi_db.status_history AS sh
        GROUP BY sh.property_id
        ) AS uhs

    INNER JOIN habi_db.property  AS p
        ON uhs.property_id = p.id

    INNER JOIN habi_db.status  AS s
        ON uhs.status_id = s.id

    WHERE
        s.name IN ('pre_venta', 'en_venta', 'vendido') AND 
        p.address <> '' AND
        p.city <> ''
"""

all_properties = f"""
    {base_query}
"""

pre_sale_properties = f"""
    {base_query} AND
    s.name = 'pre_venta'

"""

on_sale_properties = f"""
    {base_query} AND
    s.name = 'en_venta'

"""

sold_properties = f"""
    {base_query} AND
    s.name = 'vendido'

"""

