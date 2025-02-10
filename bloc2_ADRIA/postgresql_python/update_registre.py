import connect

def update_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_update ='''
    UPDATE clientes
    SET teléfono_cliente='000000000', dirección_cliente='carrer de Barcelona', correo_electrónico_cliente='correu@gmail.com'
    WHERE dirección_cliente='carrer el que sigui' AND teléfono_cliente='678113452' AND correo_electrónico_cliente='correu@correu.com'
    '''
    cursor.execute(sql_update)
    conn.commit()

    cursor.close()
    conn.close()

    return {"Update successfully"}